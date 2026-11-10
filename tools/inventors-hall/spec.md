# Inventors Hall

## One idea
In a museum hallway with empty plinths along a timeline floor, the curator, Dr. Osei (made up, labeled "illustration"), hands the child a crate of computing inventions to set up, and each one is unpacked with three clue cards (the problem, the people, the year range) and placed on the floor timeline: Jacquard's punch-card loom (1804), ENIAC (1945), the A-0 compiler from Grace Hopper's team (1952), the first swappable game cartridge console (1976), and a talking calculator for blind users (1970s); a "before and after" drawer shows what daily life could not do before (weavers set every pattern by hand; programmers wrote raw machine code), and a "who else?" button reveals people left off the plaque, such as Basile Bouchon, whose punched paper came before Jacquard, the six women who first programmed ENIAC, and Jerry Lawson, who led the cartridge work, so the child adds them to the plaque; fourth graders weigh each invention's cost card against its benefits for different groups (the loom put some hand weavers out of work, and weavers in Lyon protested), and fifth graders trace one thread across three exhibits, punch cards to programs to games, explaining how each built on the last; at the end the finished hall shows that each invention answered a real need, came from many people, and changed some lives for the worse as well as the better, so a student in grades 3 to 5 learns how computing changed daily life, why people built it, and whose ideas were included.

## Not like
- attic-gadget-box (K, spec): old gadget to new device. Here inventors and whose ideas were left out.
- eras-of-computing (6, concept): eras and a local debate. Here single inventions.
- job-shadow-day (3, concept): computing at work today. Here computing history.
- biased-bot (4, spec): unfair training data. Here people left out of the record.

## Who and how
- Grades 3-5, Computer Science, module "Computing Inventions and Inventors". Standards: E3-SOC-HI-16, E3-SOC-HU-18, E4-SOC-HI-16, E4-SOC-ET-17, E5-SOC-HI-16 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "How computing changed daily life, why people built it, and whose ideas were included").
- Format: timeline. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card and plaque. Controls 48 px or more.
- Five exhibits with clue cards, drawers, "who else?" plaques and cost cards, one thread to trace. Extra: Gallery walk (the class reads plaques aloud on the projector). tool.json `modes: ["Hall", "Gallery walk"]`, `minutes: "20-30"`, `grades_label: "Grades 3-5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| E3-SOC-HI-16, E4-SOC-HI-16 | Place exhibits; open before and after | the timeline floor; drawers | 2 |
| E3-SOC-HU-18 | Read why each was built and whose need it served | the talking calculator's users | 2 |
| E4-SOC-ET-17 | Weigh cost cards | who gained, who lost | 3 |
| E5-SOC-HI-16 | Trace one thread across three exhibits | punch cards to programs to games | 4 |

## Screens and modes
Header (kit): title "Inventors Hall"; `Hall`, `Gallery walk`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A grand museum hallway, a timeline floor with decades marked, empty plinths, a wooden crate, and Dr. Osei with a clipboard. The welcome is queued (`welcomeAfter: true`): "Help me set up the hall. Tap the crate to unpack an exhibit." First hint: "Tap the crate."

**Place (focus: the floor).** At 1366x768 the hall fills the view with clue cards in a side panel; at 680x425 the panel is a sheet. The child reads three clues and drags the exhibit onto the floor; it snaps to its year with a plaque.

**Before and after.** Each plinth has a drawer; opening it shows two small scenes and one spoken line for each.

**Who else?** The plaque names one person or company. `Who else?` reveals people whose work was left off; the child drags each name onto the plaque.

**Cost card (grade 4).** Each invention has a cost card; the child sorts who gained and who lost.

**Follow the thread (grade 5).** A gold thread links three plinths; the child picks how each built on the last.

**Many hands (the aha).** Dr. Osei: "Every invention answered a need, came from many people, and changed some lives for worse as well as better."

**The end.** The finished hall with full plaques. `Print` prints the timeline.

**Gallery walk (extra).** Projector play.

## Content
- Five exhibits; every name and date is backed twice, and ranges are used where exact dates are unsure.
- Object photos come from open-access museum collections (Smithsonian, Met, Science Museum Group) checked at Build; otherwise drawn illustrations.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Exhibits can be moved until the plaque appears; names can be dragged off again.
- Keyboard: Tab to the crate, clues, the floor (arrows move along years), drawers, Who else?, plaque names and cost sorts; Enter places or picks.
- With Motion off drawers open at once.

## Look
- Accent `--brand` #7a4419 museum brown (header, plaques, buttons); gold #f4c542 (the exhibit in hand, the thread); paper #f9f2ec; ink #251405; muted #5a5149.
- Contrast (WCAG 2.1, computed): white on brand 7.87:1; brand on paper 7.10:1; ink on paper 16.04:1; muted on paper 6.99:1; ink on gold 10.93:1.
- Never color alone: added names carry a plus sign; gained and lost carry arrows.
- Different from this batch (map blue, relay purple, workday green, council red).

## Art
- People (illustrated): Dr. Osei, labeled "illustration" (Gemini, `people: true`, 1; cutout yes); real inventors as illustrated portraits labeled with their names (Gemini, `people: true`, 6).
- Public domain or open-access photos of real objects (5), checked at Build; local FLUX (`scripts/localart.py`): the hallway (1, 16:9).
- Drawn in code: the timeline floor, drawers, plaques and the thread.
About 13 images.

## Voice
Two bank voices, each unique in this batch: `calm-professor` as Dr. Osei; `curious-librarian` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.exhibit + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `unpack`: "Tap the crate."
- how `place`: "Drag the exhibit to its year."
- how `drawer`: "Tap the drawer."
- how `who`: "Tap Who else, then drag the name onto the plaque."
- how `cost`: "Drag each group to gained or lost."
- how `thread`: "Tap how this one built on the last."
- event, whole, many hands.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the timeline floor with year snapping, clue cards, drawers, plaques with addable names, cost sorts, the thread.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Place | Drag to any plinth | The floor snaps only within the clue's year range. |
| Who else | Skip the button | The plaque stays incomplete until names are added. |
| Thread | Tap any reason | Each link has one matching reason. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `unpack`; `place`; `drawer`.
2. `who`.
3. `cost`; `thread`.
4. Many hands (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| Jacquard's loom (about 1804) built on Bouchon's punched paper (1725), and Lyon weavers protested it | Science Museum Group, Jacquard loom collection entry | Essinger (2004), "Jacquard's Web", Oxford University Press | yes |
| Six women were ENIAC's first programmers | Computer History Museum, ENIAC entries | U.S. Army and Penn Engineering, ENIAC history pages | yes |
| Grace Hopper's team built the A-0 compiler in 1952 | Computer History Museum, Grace Hopper biography | Smithsonian National Museum of American History, Grace Hopper collection | yes |
| Jerry Lawson led the Fairchild Channel F cartridge console (1976) | Computer History Museum, Jerry Lawson entry | Strong National Museum of Play, World Video Game Hall of Fame materials | yes |
Backed twice: 5. Cut: 0.

Sensitivity: people left out of history (women, a Black engineer, the weavers); a fresh-agent review before Live checks that each is shown with dignity, not as a token.

Checks run (Python, scratchpad s23, 2026-11-10): years sort as 1725, 1804, 1945, 1952, 1976; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 hall and panel; at 680x425 panel as a sheet.
2. Five exhibits are placed with before and after read, and whose need each served. (E3-SOC-HI-16, E3-SOC-HU-18, E4-SOC-HI-16)
3. Cost cards are weighed for different groups. (E4-SOC-ET-17)
4. One thread is traced across three exhibits. (E5-SOC-HI-16)
5. Every name and date is backed twice; object photos are open access.
6. `Read` reads every card and plaque; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: drawers open at once; no network requests.

## Open questions
- The talking calculator exhibit (default used: a 1970s talking calculator for blind users shown with a date range and no maker named until two sources agree).
