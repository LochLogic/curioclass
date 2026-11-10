# Shadow Puppet Studio

## One idea
The student puts on a shadow puppet show, starting in a dark room with a puppet theater where nothing can be seen; turning on a flashlight and moving it around shows that only the things it lights can be seen, and a closed box hides a toy until a light goes in, so seeing needs light; then the student holds cutouts made of cardboard, wax paper, clear plastic and foil in the beam, and a sorting tray fills with what each does: blocks light (a dark shadow), lets some light through (a soft glow), lets light through (almost no shadow) or bounces light (a bright spot on the wall); moving the light closer makes the shadow grow; at the end the student makes a short show with a cardboard hero, a wax-paper moon, a clear-plastic window and a foil mirror that bounces light onto the hero, and plays it back, so a first grader learns that objects can be seen only when lit, and what different materials do to a beam of light.

## Not like
- vibration-station (1, spec): sound. Here light.
- sky-diary (1, concept): sun and moon patterns. Here a flashlight beam.
- shade-builder (K, spec): sunlight warming. Here light and seeing.
- nature-inventor (1, concept): copying nature to solve problems. Here materials and light.

## Who and how
- Grade 1, Science, module "Light and Shadows". Standards: 1-PS4-2 (make observations to construct an evidence-based account that objects in darkness can be seen only when illuminated), 1-PS4-3 (plan and conduct investigations to determine the effect of placing objects made with different materials in the path of a beam of light).
- Format: studio. Driver: one child alone or with a grown-up nearby (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- The dark room and closed box, four materials tested in the beam, the distance test, the show. Extra: Show time (play the show full screen on the projector). tool.json `modes: ["Studio", "Show time"]`, `minutes: "15-20"`, `grades_label: "Grade 1"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 1-PS4-2 | Move the flashlight in the dark room; shine into the closed box | only lit things show; the toy appears when lit | 2 |
| 1-PS4-3 | Hold each material in the beam and sort it by what light does | shadows, glows and bright spots; the sorting tray | 3 |
| 1-PS4-3 (plan) | Choose one change (material or distance), predict, then test | the shadow growing as the light comes closer | 4 |

## Screens and modes
Header (kit): title "Shadow Puppet Studio"; `Studio`, `Show time`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** A black screen with a dim outline of a flashlight button. The welcome is queued (`welcomeAfter: true`): "It's very dark in here. Can you see anything? Tap the flashlight." First hint: "Tap the flashlight."

**The dark room (1-PS4-2).** At 1366x768 the room fills the screen; at 680x425 the same with smaller props. The flashlight makes a circle of light that follows a drag; inside the circle the puppet theater, a chair and a teddy bear show; outside stays dark. A closed box: tapping it shows nothing inside until the student opens a small hole and shines the light in, and a toy car appears. The narrator: "You see things when light shines on them."

**Material tests (focus: the beam).** The theater screen and the flashlight. Four cutouts (cardboard, wax paper, clear plastic, foil) wait in a tray. The student first predicts with a face (dark shadow, soft glow, almost nothing, bright spot), then drags each into the beam. The sorting tray fills: Blocks light, Lets some light through, Lets light through, Bounces light. A slider moves the flashlight closer or farther; the shadow grows as the light comes closer.

**The show (the aha).** A stage with four slots: hero (cardboard), moon (wax paper), window (clear plastic), mirror (foil). The student places each, then records a short show by moving the hero and the light; the foil bounces a spot onto the hero. `Play` plays it back. Narrator: "Cardboard blocks the light. Wax paper lets some through. Clear plastic lets it through. Foil bounces it. You used all four."

**The end.** The sorting tray and the show. `Print` prints the tray as a picture page.

**Show time (extra).** The show plays full screen for the class.

## Content
- The dark room with three props and the closed box, four materials, the distance slider, the four-slot stage and recording.
- No flashing light; brightness changes are gentle.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The beam and shadows are drawn in code and follow the light exactly.
- Keyboard: Tab to the flashlight, cutouts, the slider and stage slots; arrow keys move the light; Enter places.
- With Motion off the light jumps between positions and the show plays as still frames.

## Look
- Accent `--brand` #2d2a6e night indigo (header, the theater frame, the tray); gold #f4c542 (the flashlight beam, the item in hand); paper #f2f2fa; ink #0f0e26; muted #54536a.
- Contrast (WCAG 2.1, computed): white on brand 12.59:1; brand on paper 11.31:1; ink on paper 16.97:1; muted on paper 6.68:1; ink on gold 11.62:1.
- Never color alone: tray columns carry pictures and spoken names; shadows differ in shape and darkness.
- Different from this batch (pond green, sun orange, sky blue, snail plum).

## Art
- Local FLUX (`scripts/localart.py`): the puppet theater (1, 16:9), the room with a chair and teddy bear (1, 16:9).
- Illustrated puppet characters: the hero and three friends (Gemini, 4; cutout yes).
- Drawn in code: the beam, shadows, glows, the bright spot, the box, the tray.
About 6 images.

## Voice
Two bank voices, each unique in this batch: `smooth-narrator` as the theater narrator; `bright-teacher` as the studio guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.material + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `shine`: "Drag the light around the room."
- how `box`: "Shine the light into the box."
- how `predict`: "Tap what you think this will do."
- how `test`: "Drag it into the beam."
- event, whole, each material's result.
- how `show`: "Place your puppets, then tap Record."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the light and shadow drawing, the box, the tray, the stage and recording.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Dark room | Skip it | The material tests open after the box is lit. |
| Tests | Drop all four in one column | Each material lands only in the column its result shows. |
| Show | Put foil as the hero | The show plays, but the narrator asks why the hero has no shadow and points to the tray. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `shine`; `box`.
2. `predict`; `test`; result (whole), waits.
3. `show`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 1-PS4-2, 1-PS4-3 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| We see objects when light from them reaches our eyes | NASA Science, "Visible Light" | Exploratorium, "Seeing the Light" | yes |
| Opaque, translucent, transparent and reflective materials | Science Buddies, "Light: Transparent, Translucent, and Opaque" | Smithsonian Science Education Center, "Light and Shadows" | yes |
| A shadow grows as the light moves closer to the object | Exploratorium, "Shadow Play" | Science Buddies, "Shadow Size" | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad r25, 2026-11-09): four materials and four tray columns, one each; a puppet halfway between the light and the screen casts a shadow twice its size; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the room; at 680x425 smaller props.
2. Only lit things show, and the toy in the box appears only when lit. (1-PS4-2)
3. Four materials are tested in the beam and sorted by what light does. (1-PS4-3)
4. A predicted change of distance is tested and the shadow grows. (1-PS4-3)
5. The show uses all four materials and plays back.
6. No flashing light; every card is spoken.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still frames; no network requests.

## Open questions
None.
