# Inside the Keypress

## One idea
A laptop sliced open like a dollhouse, every part labeled, waits on the desk, and Zip, a glowing signal token (an illustrated character), invites the child to press the A key and follow it: the keypress becomes Zip and travels from the key to the processor, which reads the app's instruction ("show the letter"), stores the letter in memory, and lights the pixels on the screen, with every stop tappable for a one-line explanation; snapping a photo sends Zip from the camera instead; then the child swaps the app, and the same A key in a drawing app picks the eraser and in a game makes the character jump, so the hardware path stays the same while the instructions change what it means; fix-it rounds leave the screen blank, and the child checks each stop in order (cable loose, app frozen, memory full, brightness at zero), finding and fixing the one that is stuck, and fifth graders say whether the broken step was hardware or software; at the end the child sees that hardware carries the signal and software decides what it means, and that finding a problem means checking each step in order, so a student in grades 3 to 5 learns what software does, how it works with hardware, and how to fix a stuck step.

## Not like
- computer-builder (1, live): parts and what each does. Here a signal moving through the parts.
- input-or-output (2, spec): naming inputs and outputs. Here the path between them.
- network-help-desk (4, spec): network and login problems. Here problems inside one device.
- adventure-outline-cards (3, concept): planning algorithms. Here hardware and software together.

## Who and how
- Grades 3-5, Computer Science, module "Hardware and Software Together". Standards: E3-SYS-HW-12, E4-SYS-HW-12, E5-SYS-HW-12 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "What software does, how it works with hardware, and fixing a stuck step").
- Format: explorer. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every label and card. Controls 48 px or more.
- Two inputs (key, camera), five stops, three apps, six fix-it rounds. Extra: Help desk (the class calls out the next stop to check on the projector). tool.json `modes: ["Explore", "Help desk"]`, `minutes: "15-25"`, `grades_label: "Grades 3-5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| E3-SYS-HW-12 | Follow the keypress; tap each stop | Zip moving through the parts | 2 |
| E4-SYS-HW-12 | Swap apps with the same key | eraser, jump, letter | 3 |
| E5-SYS-HW-12 | Check stops in order; fix; name hardware or software | the stuck stop | 4 |

## Screens and modes
Header (kit): title "Inside the Keypress"; `Explore`, `Help desk`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A cutaway laptop on a desk with the keyboard, camera, processor, memory, an app card and the screen labeled, and Zip glowing on the A key. The welcome is queued (`welcomeAfter: true`): "Press the A key and follow me!" First hint: "Tap the A key."

**Follow (focus: the cutaway).** At 1366x768 the cutaway fills the view with the stop card on the right; at 680x425 the card is a sheet. Zip travels stop by stop, pausing at each for a tap. Each stop speaks one line ("The processor reads the app's instruction."). `Camera` repeats the trip from the camera.

**Swap the app.** Three app cards: typing, drawing, game. The child drops one into the app slot and presses A again; the path lights the same, and the screen does something different. A two-column card asks what stayed the same and what changed.

**Fix it.** The screen stays blank. Five stop buttons; the child checks them in order and the tool counts how many checks it took. Fixes: plug in the cable, close the frozen app, clear memory, turn brightness up, restart. Grade 5 labels each fault hardware or software.

**Same path, new meaning (the aha).** Zip: "The hardware carries me. The software decides what I mean."

**The end.** A trip map and the fix log. `Print` prints them.

**Help desk (extra).** Class troubleshooting.

## Content
- Five stops and six faults; parts are simplified and named the way a manual would.
- No brands; the laptop is generic.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Zip can be sent again any time; checks can be done in any order, but the log notes order.
- Keyboard: Tab to the A key, the camera, each stop, app cards, the app slot and stop buttons; Enter presses or checks.
- With Motion off Zip jumps between stops.

## Look
- Accent `--brand` #245a8f circuit blue (header, wires, buttons); gold #f4c542 (Zip, the stop in focus); paper #eef3f9; ink #081a2d; muted #4b5462.
- Contrast (WCAG 2.1, computed): white on brand 7.16:1; brand on paper 6.42:1; ink on paper 15.74:1; muted on paper 6.86:1; ink on gold 10.80:1.
- Never color alone: stops carry labels; stuck stops show a warning icon and the word "stuck".
- Different from this batch (kitchen-table rust, corkboard violet, ramp green, helper teal).

## Art
- Local FLUX (`scripts/localart.py`): the cutaway laptop in a bright clean style (1, 16:9).
- Drawn in code: Zip, the path, stop cards, app cards and the screen content.
About 1 image.

## Voice
Two bank voices, each unique in this batch: `playful-friend` as Zip; `clear-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.stop + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `press`: "Tap the A key."
- how `stop`: "Tap the stop to hear what it does."
- how `swap`: "Drag an app card into the slot, then tap the A key."
- how `check`: "Tap the next stop to check."
- how `kind`: "Tap hardware or software."
- event, whole, same path, new meaning.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the stop path as an ordered list, app instruction tables, fault seeding, the check counter.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Follow | Skip taps | The trip map fills only when each stop is heard. |
| Swap | Swap without comparing | The same-and-changed card must be filled. |
| Fix | Restart every time | Restart fixes only the frozen app; the log shows the checks. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `press`; `stop`.
2. `swap`.
3. `check`; `kind`.
4. Same path, new meaning (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| Input, processing, memory and output work together, with software giving instructions | K-12 Computer Science Framework (2016), Computing Systems, "Hardware and Software", grades 3-5 | CSTA K-12 Computer Science Standards (2017), 1B-CS-01 and 1B-CS-02 | yes |
| Troubleshooting checks steps in order | CSTA K-12 Computer Science Standards (2017), 1B-CS-03 | K-12 Computer Science Framework (2016), Computing Systems, "Troubleshooting" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s24, 2026-11-10): five stops and six faults, each fault fixed at exactly one stop; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 cutaway and card; at 680x425 card as a sheet.
2. The keypress and the photo are followed through every stop. (E3-SYS-HW-12)
3. Three apps are swapped and the same-and-changed card is filled. (E4-SYS-HW-12)
4. Six faults are found in order, fixed, and labeled hardware or software. (E5-SYS-HW-12)
5. No brand names.
6. `Read` reads every label and card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: Zip jumps; no network requests.

## Open questions
- Overlap with network-help-desk, which also lists E4-SYS-HW-12 and troubleshooting (default used: keep; this one stays inside one device).
