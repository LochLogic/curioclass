# Team Code Relay

## One idea
The screen splits into three lanes with name tags, Ana (movement), Theo (score) and You (sound), two illustrated teammates (made up, labeled "illustration") building a small catch-the-apple game together, and the child builds the sound part in blocks (a pop when an apple is caught, a buzz when one is missed) while the other lanes fill in; pressing `Join` snaps the three parts together and the game breaks in ways that show on screen: Ana's part and a leftover test in Theo's part both move the basket on the arrow keys, so it zooms twice as fast, and Theo counts "points" while the display shows "score", so the number stays at 0; the child opens each teammate's code, adds comments where the clash is, and reads replies in comments; Ana and Theo each propose a fix, the child runs both, picks one and says why; then the child gives each teammate feedback from sentence starters ("I like how... Could you...?"), hears how each one takes it, and sees vague or unkind feedback land badly; fourth graders fold a teammate's part into their own with the credit kept in a comment, and fifth graders explain an uncommented part in a comment and check it by running it; at the end the joined game works only after reading each other's code, agreeing on names and talking it through, so a student in grades 3 to 5 learns to build, read, comment, combine and give feedback on code as a team.

## Not like
- game-remix (5, live): remixing a whole game. Here joining three parts.
- code-tracer (4, live): tracing values alone. Here reading teammates' code.
- sprint-board (Grades 9-12, spec): team sprints. Here one small game.
- three-route-rules (3, concept): comparing rules. Here combining code.

## Who and how
- Grades 3-5, Computer Science, module "Code as a Team". Standards: E3-PRO-PD-05, E3-PRO-RD-07, E4-PRO-PD-04, E4-PRO-PD-05, E5-PRO-PD-05, E5-PRO-RD-07 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "Read, comment, compare and combine code with teammates").
- Format: builder. Driver: one student alone (tool.json `driver: "student"`); class mode passes one device among two or three. `Read` reads every block and comment. Controls 48 px or more.
- Three levels (sound part; fold in a teammate's part; explain uncommented code), two joins that break, two fix pairs, the feedback round. Extra: Real team (two or three students each take a lane on one device). tool.json `modes: ["Relay", "Real team"]`, `minutes: "25-35"`, `grades_label: "Grades 3-5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| E3-PRO-PD-05 | Build one part; join the work | three lanes snapping together | 2 |
| E3-PRO-RD-07, E5-PRO-RD-07 | Comment blocks; explain uncommented code | comments beside blocks | 3 |
| E4-PRO-PD-04, E4-PRO-PD-05 | Fold in a part with credit; compare fixes | two fixes running side by side | 3 |
| E5-PRO-PD-05 | Give and take feedback | teammates' replies | 4 |

## Screens and modes
Header (kit): title "Team Code Relay"; `Relay`, `Real team`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A bright team room with three desks, a big screen split into three lanes, and Ana and Theo waving from their lanes. The welcome is queued (`welcomeAfter: true`): "We each build a part, then join them. Build the sound part. Drag a block into your lane." First hint: "Drag a block into your lane."

**Build (focus: your lane).** At 1366x768 three lanes sit side by side with the game preview below; at 680x425 one lane shows at a time with tabs. Blocks: when caught, when missed, play sound, set, change, say. A `Try my part` button runs the sound part alone.

**Join.** `Join` snaps the lanes; the game runs and breaks (fast basket; score stuck at 0). A bug card names what the child saw, not the cause.

**Read and comment.** The child opens a lane, taps a block, and adds a comment from a short list or typed. Teammates reply in comments ("Oops, I left a test in!").

**Compare fixes.** Ana's fix and Theo's fix run side by side; the child picks one with a reason.

**Feedback.** Sentence starters build a note to each teammate. Kind and specific notes get a thank-you and a change; vague or unkind ones get a confused or hurt reply, and the child can try again.

**We read each other (the aha).** Ana: "It only worked once we read each other's code and agreed on names."

**The end.** The working game and the comment log. `Print` prints the code with comments.

**Real team (extra).** Lanes for real students.

## Content
- Blocks in plain words; typed comments stay on the device and are not shared.
- Teammates are labeled "illustration"; feedback replies model calm responses.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Blocks and comments can be changed until `Join`; joins can be re-run.
- Keyboard: Tab to the block palette, lanes, blocks (arrows move, Enter drops), comment boxes, fix buttons and starters; Enter runs or picks.
- With Motion off the game preview steps one frame per tap.

## Look
- Accent `--brand` #6a3d9a relay purple (header, your lane, buttons); gold #f4c542 (the block in hand, the clash spot); paper #f4effa; ink #1c0d2e; muted #55505d.
- Contrast (WCAG 2.1, computed): white on brand 7.64:1; brand on paper 6.76:1; ink on paper 16.20:1; muted on paper 6.90:1; ink on gold 11.26:1.
- Never color alone: lanes carry name tags; comments carry a speech icon.
- Different from this batch (map blue, museum brown, workday green, council red).

## Art
- People (illustrated): Ana and Theo, labeled "illustration" (Gemini, `people: true`, 2; cutout yes).
- Local FLUX (`scripts/localart.py`): the team room (1, 16:9).
- Drawn in code: blocks, lanes, the game and comments.
About 3 images.

## Voice
Two bank voices, each unique in this batch: `casual-peer` as Ana; `upbeat-guide` as Theo and the hints. `Curio.voice` with `scope: () => state.mode + ':' + state.level + ':' + state.lane + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `build`: "Drag a block into your lane."
- how `join`: "Tap Join."
- how `comment`: "Tap a block, then add a comment."
- how `fix`: "Run both fixes, then pick one."
- how `feedback`: "Pick a starter and finish your note."
- event, whole, we read each other.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: a tiny block language with events and variables, three lanes merged into one program, a seeded clash per level, side-by-side runs, comment threads, the feedback responder.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Join | Delete teammates' blocks | Their parts must still run in the joined game. |
| Comments | Comment anywhere | A comment must sit on a clashing block. |
| Feedback | Pick any starter | Vague notes get a confused reply and must be redone. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `build`; `join`.
2. `comment`; `fix`.
3. `feedback`.
4. We read each other (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| Commenting, combining and crediting code are grade 3-5 practices | CSTA K-12 Computer Science Standards (2017), 1B-AP-12, 1B-AP-14 and 1B-AP-17 | K-12 Computer Science Framework (2016), Practice 2, "Collaborating Around Computing" | yes |
| Specific, kind peer feedback improves student work | Hattie and Timperley (2007), "The Power of Feedback", Review of Educational Research | Berger, Rugen and Woodfin (2014), "Leaders of Their Own Learning", EL Education | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s23, 2026-11-10): two move handlers make the basket move 2 steps per key press against 1; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 three lanes and preview; at 680x425 lanes as tabs.
2. The sound part is built and joined with teammates' parts. (E3-PRO-PD-05)
3. Clashes are commented, a part is folded in with credit, and fixes are compared. (E3-PRO-RD-07, E4-PRO-PD-04, E4-PRO-PD-05)
4. Uncommented code is explained and checked, and feedback is given kindly and specifically. (E5-PRO-RD-07, E5-PRO-PD-05)
5. Typed comments stay on the device.
6. `Read` reads every block and comment; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: the preview steps; no network requests.

## Open questions
None.
