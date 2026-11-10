# Attic Gadget Box

## One idea
Up in a grandparent's dusty attic, Grandma Rosa (made up, labeled "illustration") hands the child a closed cardboard box, and each gadget lifted out (a rotary phone, a paper road map, a cassette player, a film camera) tells in one spoken line what job it did ("This phone called my sister. You had to dial every number."), then slides along a then-to-now track through one or two in-between versions until it lands on the device that does the same job today, so the job stays the same while the device changes; a "who made it better" card follows each move, a short illustrated story of a real person or team who saw a problem and changed the device on purpose, such as Lou Ottens and his team at Philips making the small cassette in 1963 so music could go anywhere, Steven Sasson at Kodak building the first digital camera in 1975, Gladys West's careful math of Earth's shape that GPS maps rely on, and TV captions first shown on national shows in 1980 so people who are deaf or hard of hearing could follow; first graders order three devices for one job, and second graders say what changed for the family at each step (faster, smaller, new problems like losing it) and pick whose need a change served before the story card; at the end the shelf shows every job twice, then and now, so a child in kindergarten to grade 2 learns how everyday computing changed over time and that people designed those changes for real people's needs.

## Not like
- inventors-hall (3, concept): inventors and whose ideas were left out. Here then and now for one job at a time.
- who-uses-this-device (K, concept): devices at work today. Here how devices changed.
- computer-builder (1, live): the parts of a computer. Here the history of everyday gadgets.
- wonder-wall (Grades K-2, live): ways to find answers. Here a timeline of devices.

## Who and how
- Grades K-2, Computer Science, module "Computing Then and Now". Standards: EK-SOC-HI-14, EK-SOC-HU-15, E1-SOC-HI-14, E2-SOC-HI-14, E2-SOC-HU-15 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "How everyday computing changed over time and the people who designed it").
- Format: timeline. Driver: one student alone (tool.json `driver: "student"`). Every word is spoken; `Read` reads every card. Controls 60 px or more.
- Six gadgets (phone, map, music player, camera, TV, letter), one track each with one or two in-between versions, six designer cards. Extra: Class attic (the class guesses each gadget's job before it is spoken). tool.json `modes: ["Attic", "Class attic"]`, `minutes: "10-20"`, `grades_label: "Grades K-2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| EK-SOC-HI-14 | Slide each gadget to today's device | the same job, two devices | 2 |
| E1-SOC-HI-14 | Order three devices for one job | the in-between version | 2 |
| E2-SOC-HI-14 | Pick what changed at each step | faster, smaller, new problems | 3 |
| EK-SOC-HU-15, E2-SOC-HU-15 | Meet the designer; pick whose need it served | the "who made it better" card | 4 |

## Screens and modes
Header (kit): title "Attic Gadget Box"; `Attic`, `Class attic`; `Read`, `Motion`, `Sound`, `Print`. Controls 60 px or more.

**On load and first tap.** A warm attic with a round window, dust in the light, a closed cardboard box, and Grandma Rosa in a rocking chair. The welcome is queued (`welcomeAfter: true`): "What's in my old box? Tap the box to open it." First hint: "Tap the box."

**Lift (focus: the box).** At 1366x768 the attic is above with the track along the bottom; at 680x425 the track scrolls sideways. A gadget rises from the box and Grandma Rosa says its job.

**Slide.** The child drags the gadget along the track; at each stop it changes into the next version (rotary phone, push-button phone, today's phone). Kindergarten has two stops; grades 1 and 2 have three, and the child puts them in order first.

**What changed (grade 2).** At each stop, two or three picture choices: faster, smaller, works anywhere, new problem. The child taps the ones that fit.

**Who made it better.** A storybook card with the person or team, the problem they saw and what they changed, spoken in three short lines. Grade 2 first picks whose need the change served from two or three pictures.

**Then and now (the aha).** Grandma Rosa: "Every job is still here. People changed the tools on purpose, to help other people."

**The end.** The shelf with every job twice. `Print` prints a then-and-now sheet.

**Class attic (extra).** Projector play.

## Content
- Six gadgets with sourced designer cards; names and dates appear only when confirmed by two sources.
- Grandma Rosa is a made-up character, labeled "illustration"; designers are real people, drawn as illustrations and labeled with their names.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A gadget can be slid back and forth until it lands.
- Keyboard: Tab to the box, the gadget, track stops (arrows move along the track), choice pictures and the card; Enter lifts, drops or picks.
- With Motion off gadgets change at once and dust does not drift.

## Look
- Accent `--brand` #8e3b5a attic rose (header, the track, buttons); gold #f4c542 (the gadget in hand, today's stop); paper #faf0f3; ink #2b0c18; muted #5d4f54.
- Contrast (WCAG 2.1, computed): white on brand 7.18:1; brand on paper 6.44:1; ink on paper 16.11:1; muted on paper 6.94:1; ink on gold 11.05:1.
- Never color alone: track stops carry "then" and "now" labels and a clock icon.
- Different from this batch (honey brown, street-fair green, board blue, bamboo teal).

## Art
- People (illustrated): Grandma Rosa, labeled "illustration", and six designer portraits labeled with each real name (Gemini, `people: true`, 7; cutout yes).
- Local FLUX (`scripts/localart.py`): the attic (1, 16:9), gadgets old and new (14, 1:1).
- Drawn in code: the track, stops and choice icons.
About 22 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as Grandma Rosa; `warm-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.gadget + ':' + state.stop + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `lift`: "Tap the box."
- how `slide`: "Drag it along the track."
- how `order`: "Drag them into order, oldest first."
- how `changed`: "Tap what changed."
- how `who`: "Tap whose need it helped."
- event, whole, then and now.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the gadget deck, the snapping track, the change choices, the storybook card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Order | Drop gadgets anywhere | The track snaps only to the right stop, and the order is checked. |
| What changed | Tap every choice | Each step has its own right set. |
| Whose need | Tap the first picture | The pick is checked against the card's story. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `lift`; `slide`.
2. `order`; `changed`.
3. `who`.
4. Then and now (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| Lou Ottens led the Philips team that introduced the compact cassette in 1963 | Philips company history | The New York Times obituary of Lou Ottens (2021) | yes |
| Steven Sasson built the first digital camera at Kodak in 1975 | Kodak company history | National Inventors Hall of Fame, Steven Sasson entry | yes |
| Gladys West's work modeling Earth's shape supported GPS | U.S. Air Force, Space and Missile Pioneers Hall of Fame induction (2018) | Guinness World Records and BBC profiles (2018) | yes |
| National TV shows first carried closed captions in 1980 | National Captioning Institute history | Federal Communications Commission, closed captioning history | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad s22, 2026-11-10): card dates sort as 1963, 1975, 1980, 2018, and each then device comes before its now device; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 attic and track; at 680x425 track scrolls.
2. Six gadgets slide to today's device, with three-stop orders for grades 1 and 2. (EK-SOC-HI-14, E1-SOC-HI-14)
3. Grade 2 names what changed at each step. (E2-SOC-HI-14)
4. Six designer cards are met, and grade 2 picks whose need each change served. (EK-SOC-HU-15, E2-SOC-HU-15)
5. Every name and date on a card is backed twice.
6. `Read` reads every card; every control is 60 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: gadgets change at once; no network requests.

## Open questions
- Designer cards (default used: Ottens and Philips 1963, Sasson and Kodak 1975, Gladys West and GPS, national TV captions 1980, plus the phone and letter tracks with no person named until a second source is found).
