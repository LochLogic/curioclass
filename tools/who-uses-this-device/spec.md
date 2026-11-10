# Who Uses This Device?

## One idea
On a sunny street fair lined with booths and a bus stop, the fair announcer, Mr. Dee (made up, labeled "illustration"), invites the child to tap the grown-ups at work and see the device that helps each one: the vet's scanner beeps a puppy's microchip number so the vet can look up the family, the bus driver's fare reader beeps a card, the artist's drawing tablet turns a pen line into color, the coach's stopwatch catches a runner's time, and the baker's oven timer rings; kindergartners open each device into big labeled parts (screen, buttons, camera, speaker, sensor) and tap a part to hear what it does for this job; first graders sort the devices into home, school and work, finding that some belong in more than one; second graders meet four kids who love animals, drawing, buses or sports and match each to a computing job seen at the fair, saying how the device fits; at the end a helpers page fills with every device, its parts and its job, and the child sees that computers are inside lots of jobs, not only at desks, so a child in kindergarten to grade 2 learns how people use digital devices at home, school and work, names device parts and what they do, and connects interests to computing jobs.

## Not like
- computer-builder (1, live): build a computer from parts. Here devices in real jobs.
- job-shadow-day (3, concept): a day of choices at work. Here a fair to browse.
- industry-device-tour (6, concept): input to output in industry machines. Here simple parts for young kids.
- me-vs-the-counter (K, spec): hand counts against a computer. Here devices people use.

## Who and how
- Grades K-2, Computer Science, module "Devices at Home, School and Work". Standards: EK-SOC-CE-16, EK-SYS-HW-11, E1-SOC-CE-16, E2-SOC-CE-16 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "How people use digital devices and tools, and jobs that match what you love").
- Format: explorer. Driver: one student alone (tool.json `driver: "student"`). Every word is spoken; `Read` reads every card. Controls 60 px or more.
- Eight workers and devices, a parts view for each, a home-school-work sort, four hobby matches. Extra: Class fair (the teacher taps workers on the projector while the class guesses the device). tool.json `modes: ["Fair", "Class fair"]`, `minutes: "10-20"`, `grades_label: "Grades K-2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| EK-SOC-CE-16 | Tap workers; watch the device help | the device doing its job | 2 |
| EK-SYS-HW-11 | Open a device; tap its parts | big labeled parts | 2 |
| E1-SOC-CE-16 | Sort devices into home, school, work | some in more than one place | 3 |
| E2-SOC-CE-16 | Match a hobby to a computing job | four kids and their matches | 4 |

## Screens and modes
Header (kit): title "Who Uses This Device?"; `Fair`, `Class fair`; `Read`, `Motion`, `Sound`, `Print`. Controls 60 px or more.

**On load and first tap.** A sunny street with striped booths, balloons, a bus at the stop, and Mr. Dee with a microphone. The welcome is queued (`welcomeAfter: true`): "Everyone here has a helper. Tap a person to see theirs." First hint: "Tap a person."

**Fair (focus: the street).** At 1366x768 the street fills the view with the helpers page as a side strip; at 680x425 the street scrolls and the page is a tab. Workers: vet, bus driver, artist, coach, baker, librarian (barcode scanner), farmer (weather app), nurse (thermometer). Tapping one plays a short scene of the device at work.

**Look inside.** `Open it` splits the device into parts; each part glows and speaks its job ("The speaker beeps so the driver knows the card worked.").

**Where it lives (grade 1).** Three houses: home, school, work. The child drags each device; some fit two or three, and the device copies itself into each house.

**Hobby match (grade 2).** Four kids with hobbies. The child drags each kid to a worker, then picks how the device fits from two pictures.

**Computers everywhere (the aha).** Mr. Dee: "Computers are inside lots of jobs. Not just at desks!"

**The end.** The filled helpers page. `Print` prints it.

**Class fair (extra).** Projector play.

## Content
- Eight workers in varied skin tones, ages and abilities (one coach uses a wheelchair), labeled "illustration", all spoken.
- The microchip scene shows a number, not a family's name, because the vet looks the number up.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Parts can be tapped in any order; sorts and matches can be redone.
- Keyboard: Tab to each worker, Open it, parts, houses and kids; Enter opens, drops or picks.
- With Motion off scenes show their last frame and parts split at once.

## Look
- Accent `--brand` #1f6b3a street-fair green (header, the helpers page, buttons); gold #f4c542 (the part in focus, a matched kid); paper #eef7f0; ink #06200f; muted #4a574e.
- Contrast (WCAG 2.1, computed): white on brand 6.52:1; brand on paper 5.96:1; ink on paper 15.72:1; muted on paper 6.94:1; ink on gold 10.57:1.
- Never color alone: houses carry pictures and spoken names; parts carry labels.
- Different from this batch (honey brown, attic rose, board blue, bamboo teal).

## Art
- People (illustrated): Mr. Dee, eight workers and four kids, labeled "illustration" (Gemini, `people: true`, 13; cutout yes).
- Local FLUX (`scripts/localart.py`): the street fair (1, 16:9).
- Drawn in code: device parts, houses and the helpers page, so parts read clearly.
About 14 images.

## Voice
Two bank voices, each unique in this batch: `lively-host` as Mr. Dee; `easy-coach` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.worker + ':' + state.part + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `tap`: "Tap a person."
- how `open`: "Tap Open it."
- how `part`: "Tap a part to hear what it does."
- how `sort`: "Drag the device to a house."
- how `match`: "Drag the kid to a worker."
- event, whole, computers everywhere.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the scrolling street, device scenes, the parts splitter, multi-house sort, hobby matches.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Parts | Skip parts | The page fills only after each device's parts are heard. |
| Sort | Put every device at work | Home and school devices stay unsorted until placed. |
| Match | Drag kids anywhere | Each match needs a fit picked. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `tap`; `open`; `part`.
2. `sort`.
3. `match`.
4. Computers everywhere (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| Pet microchips hold an ID number that is looked up in a registry | American Veterinary Medical Association, "Microchipping of animals" FAQ | American Kennel Club, "Pet Microchipping" | yes |
| Computing jobs exist across many fields | U.S. Bureau of Labor Statistics, Occupational Outlook Handbook | Code.org, "Computing careers" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s22, 2026-11-10): eight workers, eight devices, four kids each with one best match; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 street and page; at 680x425 street scrolls and page as a tab.
2. Eight workers' devices are seen at work and opened into parts. (EK-SOC-CE-16, EK-SYS-HW-11)
3. Devices are sorted into home, school and work, some into more than one. (E1-SOC-CE-16)
4. Four hobbies are matched to computing jobs with a reason. (E2-SOC-CE-16)
5. The cast is varied and labeled illustration.
6. `Read` reads every card; every control is 60 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: scenes show last frames; no network requests.

## Open questions
None.
