# Tablet Buddy

## One idea
The child guides Pip, a young panda (an illustrated animal character) in a class of animal friends, through one school day with the class's one shared tablet, and every choice at six moments shows what it does to Pip and to the next friend who uses it: sticky snack hands smudge the screen for Otter, a one-hand carry drops it, no headphones makes the reading corner noisy, leaving his game open lets Fox change Pip's score, and three videos in a row leave Pip's eyes tired so he misses the playground; good uses get equal time, a video call with Grandma Panda, a reading app that says a hard word aloud, a photo of the bean plant for science; kindergartners pick the careful way to hold, clean and share the tablet and see why; first graders compare a helpful use and a too-long use in the same day; second graders explain to a friend why logging out and taking turns matter by choosing the reason that matches what happened; at the end a day map shows Pip's energy and each friend's face at every moment, so a child in kindergarten to grade 2 learns to use shared devices responsibly and to weigh the benefits and harms of screen time.

## Not like
- internet-journey (4, spec): a message crossing the internet. Here caring for a shared device.
- secret-keeper (K, spec): what is OK to share. Here how to use a device well.
- habit-hero (Grades K-2, live): health habits through a day. Here device habits and screen time.
- who-uses-this-device (K, concept): devices in jobs. Here one device shared by a class.

## Who and how
- Grades K-2, Computer Science, module "Using Tech Well". Standards: EK-SYS-IM-13, E1-SYS-IM-13, E2-SYS-IM-13 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "Responsible use of shared devices; benefits and harms of screen time").
- Format: story. Driver: one student alone (tool.json `driver: "student"`). Every word is spoken; `Read` reads every choice. Controls 60 px or more.
- Six moments with two or three picture choices each, three good-use moments, the day map, a printable rules card. Extra: Our tablet rules (the class builds its own rules card on the projector). tool.json `modes: ["Pip's day", "Our tablet rules"]`, `minutes: "10-15"`, `grades_label: "Grades K-2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| EK-SYS-IM-13 | Pick how to hold, clean and share | a smudge, a drop, a friend's face | 2 |
| E1-SYS-IM-13 | Compare a helpful use with a too-long use | Pip's energy line | 3 |
| E2-SYS-IM-13 | Choose the reason that matches | Fox changing the score; the logout | 4 |

## Screens and modes
Header (kit): title "Tablet Buddy"; `Pip's day`, `Our tablet rules`; `Read`, `Motion`, `Sound`, `Print`. Controls 60 px or more.

**On load and first tap.** A cozy classroom of animal friends, the shared tablet in its charging basket, and Pip waving. The welcome is queued (`welcomeAfter: true`): "Help Pip use the tablet today. Tap the tablet to start." First hint: "Tap the tablet."

**A moment (focus: the scene).** At 1366x768 the scene fills the view with the day map as a strip on top; at 680x425 the map is a tab. Each moment speaks a short line and shows two or three picture choices (wash hands or snack hands; two hands or one; headphones or none; log out or leave it). The child taps one and sees the result for Pip and the next friend. A different choice can be tried after.

**Good uses.** Three moments where the tablet helps: the call with Grandma Panda, the reading app, the bean plant photo.

**Too long (grade 1).** After lunch Pip can watch one video and go outside, or three videos; the energy line dips and the playground empties. The child compares the two days.

**Why it matters (grade 2).** Otter asks "Why log out?"; the child picks the reason that matches what happened earlier.

**Shared with care (the aha).** Narrator: "The tablet helps when we share it with care. It can hurt when we don't."

**The end.** The day map with faces. `Print` prints the rules card from the child's best choices.

**Our tablet rules (extra).** Class rules card.

## Content
- Animal characters only, so no child is shown as careless; all spoken.
- Screen time is shown as "a long time" and "a short time", not hours, and a teacher note points to family media plans.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Every moment can be replayed with a different choice.
- Keyboard: Tab to the tablet, choice pictures, the day map moments and Print; Enter picks.
- With Motion off results show as stills.

## Look
- Accent `--brand` #0f6660 bamboo teal (header, the day map, buttons); gold #f4c542 (the choice in focus, Pip's energy line); paper #ecf6f5; ink #03201e; muted #4a5856.
- Contrast (WCAG 2.1, computed): white on brand 6.80:1; brand on paper 6.17:1; ink on paper 15.51:1; muted on paper 6.76:1; ink on gold 10.50:1.
- Never color alone: friends' faces show smiles or frowns; the energy line has a battery icon.
- Different from this batch (honey brown, attic rose, street-fair green, board blue).

## Art
- Local FLUX (`scripts/localart.py`): the classroom (1, 16:9), six moment scenes (6, 16:9), Pip, Otter, Fox and Grandma Panda (4, 1:1, cutout yes), all illustrated animals.
- Drawn in code: the day map, faces and energy line.
About 11 images.

## Voice
Two bank voices, each unique in this batch: `playful-friend` as Pip; `big-sister` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.moment + ':' + state.choice + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `start`: "Tap the tablet."
- how `choose`: "Tap a picture to choose."
- how `again`: "Tap Try again to choose the other way."
- how `compare`: "Tap the day that felt better."
- how `why`: "Tap the reason that matches."
- event, whole, shared with care.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the day as a list of moments with branches and results, the day map, the rules card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Choices | Tap anything | Every result is shown, and the day map keeps each friend's face. |
| Too long | Pick the long day | The energy line and empty playground show why. |
| Why | Tap the first reason | Each reason must match an earlier moment. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `start`; `choose`; `again`.
2. `compare`.
3. `why`.
4. Shared with care (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| Young children benefit from limits and breaks in screen time and from shared, purposeful use | American Academy of Pediatrics, "Family Media Plan" and Council on Communications and Media (2016), "Media and Young Minds" | World Health Organization (2019), "Guidelines on physical activity, sedentary behaviour and sleep for children under 5 years of age" | yes |
| Handwashing and cleaning shared surfaces reduce germ spread | Centers for Disease Control and Prevention, "When and How to Wash Your Hands" | Centers for Disease Control and Prevention, "Cleaning and Disinfecting Your Facility" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s22, 2026-11-10): six care moments and three good-use moments, nine in all; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 scene and map; at 680x425 map as a tab.
2. Six care moments are played with results for Pip and a friend. (EK-SYS-IM-13)
3. A helpful use and a too-long use are compared. (E1-SYS-IM-13)
4. Reasons for logging out and taking turns are matched to what happened. (E2-SYS-IM-13)
5. Good uses get equal time; no hours of screen time are prescribed.
6. `Read` reads every choice; every control is 60 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: results are stills; no network requests.

## Open questions
None.
