# Stage Lighting Plot

## One idea
Hang and aim real instruments over the Helmers' living room, write cues, then run the last scene of A Doll's House: a light graph under the stage traces brightness, warmth and who is lit best beat by beat against the story's turning points, so you can see whether your light turns when the story turns, and keep revising until it does.

## Not like
- stage-blocker (6-8, builder) and director-s-chair (9-12, story; the stage family): lights there are area buttons (off, half, full) serving blocking and focus. Here light is the whole subject: instrument types, positions, beam angles, gels, levels, fades and cues, with fixed blocking.
- dance-styles-explorer (9-12): a stage void for dance traces. Here the stage is a realist room and the light must seem to come from its lamp, stove and window.
- gallery-critique (9-12): talks about light in a painting. Here you make the light.
- monologue-rehearsal (this band): the actor's choices in one speech. Here the actors' moves are fixed and the designer's choices change what the audience sees.

## Who and how
- Grade 9-12, theater, module "Lighting and Technical Design (Theater)".
- Topic line: lighting design for a scene
- Driver: students on laptops, alone or in pairs. 30 to 50 minutes; the design is saved on this device.
- Standards: NCAS TH:Cr1 (envision and conceptualize a design from research), TH:Cr3 (refine a design through rehearsal), TH:Pr5 (technical elements in production).

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound`. Kit theme `theme-912`. Modes (`.seg`): `Research`, `Hang` (default), `Cues`, `Run`. A sandbox: nothing is locked, nothing is scored.

**Research.** Focus: the open research card, large and central. Five cards (Content) as a row of painted tiles; tap one to open it (picture, three short facts). Under them, `Motivation`: four toggles for where the room's light should seem to come from (`Table lamp`, `Stove`, `Window`, `Hall door`); each toggled source draws a faint arrow on the Hang plan and the Run view so the student can aim from it. Choosing is optional.

**Hang.** Focus: the ground plan, filling the stage. A top view of the room on a proscenium stage (Content "Stage"), with the set (walls, doors, window, stove, table, chairs) in code, the actors' marks for the current beat as small labeled dots (N, H), and the hanging positions as bars: `FOH` (in the house), `1st electric`, `2nd electric`, `SL boom`, `SR boom`. Panel: the instrument shelf (ERS 19°, ERS 36°, Fresnel, PAR) with each type's painted picture and how many are left, then the selected instrument's settings: channel (auto, editable 1 to 40), `Gel` (picker with swatches and names), `Gobo` (ERS only: none, window panes, leaf breakup), `Spot / Flood` (Fresnel only), `Remove`. Drag a type onto a bar to hang it (it snaps to 0.5 m steps); drag the instrument's focus point (a ring) anywhere on the plan to aim; its beam is drawn as a pool on the plan (ellipse, edge per type) and the throw and pool size show beside it ("throw 5.3 m, pool 3.4 m"). The practicals (table lamp, stove glow, window backing) are already in place as channels 41, 42, 43. `Preview` (a toggle) shows the Run view of the current beat in a corner inset (one third of the stage) that updates as you aim.

**Cues.** Focus: the board (one fader per channel) with the cue list beside it. Left: the script as eight beats (Content), current beat highlighted; tap a beat to make it current. Right: the cue list (cue number, beat, fade time, label). Board: a vertical fader 0 to 100 per hung channel, grouped by position, plus the three practicals; `All to 0`. `Record cue` stores the faders as a cue at the current beat (cue numbers 1, 2, 3 in beat order; a second cue on the same beat gets 2.5); `Update cue` and `Delete cue` for the selected cue; `Fade` (0 to 10 s, step 0.5). With Preview on, the inset shows the beat under the current faders.

**Run.** Focus: the Run view (the painted set seen from the center of the house, relit by your design), the largest thing on screen, with the light graph directly under it. `Run scene` plays the eight beats (each 5 s, captions at the bottom of the view, actors' crosses 1.2 s; the scene runs about 40 s because it is the scene), firing each cue at its beat with its fade. `Step` (next beat, firing its cue), `Back`, `Stop`, and a beat scrubber (tap any beat to jump; the look is the last cue at or before it, fully faded). The light graph: x is beats 1 to 8; three lines: `Brightness` (the mean stage level), `Warmth` (warm minus cool, from the gels), `On Nora` minus `On Helmer` (how much brighter her face is than his); each line has its own color, dash and label. Story turns are tall marks with labels on the graph (beats 2, 5 and 8, from Content); `Edit turns` lets the student move or add marks (their own reading). Under the graph, the observations (Interactions). Every control works while the scene runs and acts at once: Stop freezes on the current frame, Step and Back stop and jump, a scrubber tap jumps, and a fader change in Cues while running shows on the next frame.

## Content
**The scene.** Henrik Ibsen, A Doll's House (1879), Act III, in R. Farquharson Sharp's translation (Everyman, 1910; Project Gutenberg 2542). Cut to eight beats; [...] marks a cut. Sharp's dashes are set as commas or "..." here (house rule: no long dashes).
1. Helmer: "What is this? Not gone to bed? Have you changed your things?" Nora (in everyday dress): "Yes, Torvald, I have changed my things now." Helmer: "But what for? So late as this." Nora: "I shall not sleep tonight."
2. Nora (looking at her watch): "It is not so very late. Sit down here, Torvald. You and I have much to say to one another." (She sits down at one side of the table.) [...] "Torvald, this is a settling of accounts."
3. Nora: "We have been married now eight years. Does it not occur to you that this is the first time we two, you and I, husband and wife, have had a serious conversation?"
4. Nora: "But our home has been nothing but a playroom. I have been your doll-wife, just as at home I was papa's doll-child; and here the children have been my dolls."
5. Nora (getting up): "Torvald, it was then it dawned upon me that for eight years I had been living here with a strange man, and had borne him three children. Oh, I can't bear to think of it!"
6. Nora (putting on her cloak): "I cannot spend the night in a strange man's room."
7. Nora: "See, here is your ring back. Give me mine." Helmer: "That too?" Nora: "That too." Helmer: "Here it is."
8. Nora: "That our life together would be a real wedlock. Goodbye." (She goes out through the hall.) Helmer: "Nora! Nora! Empty. She is gone. The most wonderful thing of all...?" (The sound of a door shutting is heard from below.)
- Default story turns: beat 2 "She sits: the settling of accounts", beat 5 "She stands: she sees the marriage", beat 8 "She is gone".
- Blocking (plan meters, x 0 at center, + to house right, y 0 at the curtain line, + upstage): beat 1 Nora (-1.5, 4.2), Helmer (-2.4, 6.0) entering from the study door; 2 Nora (-0.9, 3.4) seated, Helmer (0.9, 3.4) seated; 3 and 4 the same; 5 Nora standing (-1.8, 2.6), Helmer seated (0.9, 3.4); 6 Nora (1.6, 5.0) by the hall door with cloak and hat, Helmer standing (0.4, 3.0); 7 Nora (0.2, 3.9), Helmer (0.8, 3.6); 8 Nora exits through the hall door (2.6, 6.8) in the first 1.5 s, Helmer sits on the chair at the door (2.0, 5.8). Heads at 1.6 m standing, 1.2 m seated.

**Stage.** Proscenium opening 10 m wide, 6 m high; stage 10 m wide by 7 m deep. The room: back wall at y 7 with the hall door upstage right (x 2.6) and the study door upstage left (x -2.4); the left wall has the window (y 2 to 4); the stove is downstage right (4.2, 1.8); the table (round, 1.1 m) at (0, 3.4) with chairs either side, the lamp on it. Positions (height): FOH 8 m at y -6 (x -4 to 4); 1st electric 6.5 m at y 1.5; 2nd electric 6.5 m at y 4.5 (both x -5 to 5); SL boom at x -6 and SR boom at x 6, y 0.5 to 5, heights 1 to 3 m (the student sets the height, 0.5 m steps).

**Instruments** (inventory; beam; output Φ in the model's own units; edge): ERS 19° x 4 (19°, Φ 10, hard edge; gobo slot); ERS 36° x 8 (36°, Φ 10, hard; gobo slot); Fresnel x 8 (20° spot or 50° flood, Φ 10, soft); PAR x 4 (oval 12° by 28°, Φ 14, medium edge; the long axis turns with a handle). Practicals: table lamp (ch 41, a warm glow of radius 1.2 m around the lamp plus the shade drawn bright), stove glow (ch 42, warm flicker, 0.8 m), window backing (ch 43, light behind the window, colored by its own gel, default Lee 201).

**Gels** (name; warmth score; display color, the tool's own approximation): No color (open white) 0, #fff4e0; Rosco R02 Bastard Amber +1, #ffd9a8; Rosco R33 No Color Pink +0.5, #ffd6dc; Rosco R60 No Color Blue -0.5, #d6e6ff; Lee 204 Full CT Orange +2, #ffb46b; Lee 201 Full CT Blue -2, #a9c6ff; Rosco R26 Light Red +2, #ff5b5b; Rosco R80 Primary Blue -2.5, #3b6bff.

**Research cards** (picture; facts):
1. Kerosene lamp (rs-lamp): "Ibsen's stage direction for Act III: a lamp is burning on the table." / "In 1870s homes, evening light came from oil and kerosene lamps and candles." / "Flame light is very warm in color, about 1,800 to 2,000 kelvin; daylight is far bluer, about 5,500 to 6,500 kelvin."
2. The stove (rs-stove): "Act I describes a stove downstage right, with a fire burning. It is winter." / "A fire glows low and flickers; it lights from below, not above." / "Low light on a face reads very differently from light from above."
3. Winter window (rs-window): "In late December the sun sets in Oslo (then Christiania) about 3:15 in the afternoon, after about six hours of daylight." / "This scene is late at night, after a costume party upstairs." / "Any light through the window is moonlight, snow glow or a street lamp: cool and dim."
4. The hall door (rs-hall): "Act III opens with the door into the hall standing open." / "Nora leaves through the hall; the last sound of the play is a door shutting below." / "Light spilling from a doorway can show where people come from and go."
5. The 1879 stage (rs-gaslit): "A Doll's House opened at the Royal Danish Theatre in Copenhagen on 21 December 1879." / "Stages then were lit by gas; London's Savoy Theatre was the first theater lit fully by electricity, in 1881." / "Today's designers keep the period's sources but light with modern instruments."

## Interactions in detail
- Light model ("a simple model", in a `How the light works` note): for each instrument, throw t = distance from the instrument to its focus point (the ring, at 1.6 m above the floor); pool radius r = t x tan(beam / 2) (an ellipse for the PAR and for any steep angle onto the floor); energy at the pool center E = level x Φ / (π r²) x gel transmission (no color 1.0, pale gels 0.85, R02 and R33 0.8, Lee 204 0.6, Lee 201 0.45, R26 0.3, R80 0.15); edge falloff hard (ERS: full to 0 over the outer 10% of r), medium (PAR: outer 30%), soft (Fresnel: smooth over the outer 50%). The light at a point is the sum over instruments, as color (the gel color times E); shown brightness is 1 - e^(-E) per channel, so pools add and saturate instead of clipping. Ambient 0.03.
- Run view: the painted set (Art) was painted in flat even light. The builder maps the floor and back wall in the picture to plan coordinates (four corner points each, given in the painting's own pixel frame once it is made), computes the light on a 160 x 90 buffer, blurs it 2 px, and multiplies it over the picture (plus each practical's glow added on top). Actors are code silhouettes (Nora: a long period dress, a cloak and hat from beat 6; Helmer: a tailcoat), drawn at their marks with perspective scale, filled with the light at their head point.
- Graph values per beat (the look at the end of each beat's fade): Brightness = mean shown brightness over the floor area inside the room; Warmth = intensity-weighted mean gel warmth; On Nora minus On Helmer = the difference of their head-point brightness (Nora offstage at beat 8 counts as 0).
- Observations (plain lines under the graph, never a score): "Your light changes at beats 2 and 8. The story also turns at 5." / "At beat 5 Nora is lit 0.22 brighter than Helmer." / "The light seems to come from: table lamp, window." (a source counts when an instrument within 2 m of its arrow line is at 30 or more) / "No cue at beat 8: the light holds still as she leaves." A change counts at a beat when any line moves 0.08 or more from the beat before.
- Hanging limits: one instrument per 0.5 m on a bar; a full type shows "None left: remove one to move it". Focus points can go anywhere on the stage floor; aiming outside the room shows the pool on the wall and floor of the masking (dim).
- Extremes: everything at 0 shows the stage black with only ambient and the warning "Nobody can see the actors"; all channels at 100 with Fresnels on spot shows washed-out pools, and the graph's brightness near 1.
- Cue rules: a cue holds until the next; the first cue at beat 1 fades from black over its fade time; no cue before beat 1 means the scene starts dark (and the observation says so).
- Saving: localStorage `curio-lighting-plot` (instruments, gels, focus points, practical levels, motivation toggles, cues, turn marks). `Clear design` (confirm) in Hang.
- Sizes: at 1366 x 768 the plan fills the stage with the shelf and settings in the panel; at 680 x 425 Hang shows the plan with the shelf as a single row of icons; in Run the view and graph stack with the graph at least 120 px tall at every size; at 375 wide Cues shows faders in a horizontal scroller with `Record cue` pinned.

## Look
- Kit `theme-912` base; accent (`--brand`) #ee6ff0 gel magenta. Plan: floor #1a1a20, set walls #8a8a94 lines, position bars #c9c9d2, pools as additive light over the floor, focus rings in the accent. Graph lines: Brightness #e8edf3 solid, Warmth #ffb46b dashed, Nora minus Helmer #8fe3ff dotted; turn marks in the accent with labels.
- Contrast (computed in Python): brand on panel 6.73:1; brand on section 6.38:1; brand-ink #1c1203 on brand 7.18:1.
- Different from director-s-chair (footlight orange), stage-blocker (spike orange on paper), dance-styles-explorer (lilac on a void) and every other spec in this band.

## Art
Local FLUX, no people, no lettering. 9 images, none for Gemini. webp, long side 1600 px for the set, 900 px for the rest.
- slp-set: a painting of an 1870s Norwegian middle-class living room seen straight on from the audience like a stage set, flat even light, a round table in the middle with chairs and an unlit oil lamp, a tiled stove at the right front, a window on the left wall, two doors in the back wall (the right one open to a dark hall), a piano between the doors, engravings on the walls, no ceiling; 16:9; cutout no; people no; the Run view and the Preview inset, relit in code.
- rs-lamp: a painting of a brass kerosene table lamp with a glass chimney and a white glass shade, lit, on a dark wooden table; 1:1; no; no; research card 1 and the shelf note for the practical.
- rs-stove: a painting of a tall white tiled stove with a small iron door glowing orange, in a dark room; 3:4; no; no; research card 2.
- rs-window: a painting of a frosted window at night from inside a dark room, blue snow light outside and a distant street lamp; 3:4; no; no; research card 3.
- rs-hall: a painting of a half open wooden door from a dark room into a dim hallway with a coat hook and stairs going down; 3:4; no; no; research card 4.
- rs-gaslit: a painting of an empty 1870s theater stage with a painted drawing room backdrop and a row of glowing gas footlights, seen from the stalls; 16:9; no; no; research card 5.
- slp-ers: a painting of a black ellipsoidal theater spotlight hanging from a pipe by a C clamp, side view, on a plain dark background; 4:3; cutout yes; no; the shelf.
- slp-fresnel: a painting of a black Fresnel theater lantern with a stepped glass lens and barn doors, three quarter view, on a plain dark background; 4:3; cutout yes; no; the shelf.
- slp-par: a painting of a black PAR can stage light, a simple cylinder with a lamp at the back, three quarter view, on a plain dark background; 4:3; cutout yes; no; the shelf.
- Drawn in code: the plan, symbols, beams and pools, faders, cue list, graph, the actors' silhouettes (the light on them is the point, not their faces) and every label.

## Voice
Bank voice: `gravel-ranger` (Algenib), "Say warmly with a gravelly voice, like an old park ranger telling stories", here an old master electrician who has hung a thousand shows. Not used by any 9-12 arts neighbor or another spec in this band. `Curio.voice`, scope = mode. Script lines are captions, never spoken (the student reads the scene).
- welcomeHang (how; Hang entered with nothing hung; stale once an instrument is hung): "Drag a light from the shelf onto a pipe. Then drag its ring to aim it."
- aimHow (how; the first instrument hung; stale once a ring is dragged): "Drag the ring to where you want the light to land."
- gelHow (how; the first aimed instrument with no gel; stale once a gel is chosen): "Tap Gel to color it. Warm reads like the lamp, cool like the window."
- welcomeCues (how; Cues entered with no cues; stale once a cue is recorded): "Tap a beat, set the faders, then tap Record cue."
- welcomeRun (how; Run entered; stale once Run scene or Step is tapped): "Tap Run scene, and watch the graph under the stage."
- noTurn (event; after a full run when a story turn has no change within one beat of it; stale when the mode changes): "The story turns at beat (n), but your light holds still."
- allTurns (event; after a full run when every turn has a change within one beat; stale when the mode changes): "Every turn in the story has a turn in the light."
- dark (event; each time a run reaches a beat with both actors below 0.1; stale at the next beat): "We can't see them."

## Family engine
None. The stage family's lights (kit/stage.js: area levels off, half, full) are too coarse for instruments, beam angles and gels; this tool keeps its own light model. Open question: whether the light model should move into kit/stage.js later.

## Sources
- NCAS Theatre TH:Cr1, TH:Cr3, TH:Pr5: https://www.nationalartsstandards.org/
- Text, stage directions (lamp burning on the table; hall door open; stove downstage right, fire burning, winter; door shutting below): Ibsen, A Doll's House, trans. R. Farquharson Sharp, Project Gutenberg eBook 2542, https://www.gutenberg.org/ebooks/2542 (read 2026-10-29; public domain).
- Premiere at the Royal Danish Theatre, Copenhagen, 21 December 1879: Encyclopaedia Britannica, "A Doll's House", https://www.britannica.com/topic/A-Doll-s-House
- Savoy Theatre, first public building lit entirely by electricity, 1881: Encyclopaedia Britannica, "Savoy Theatre"; Victoria and Albert Museum, "The Savoy Theatre".
- Flame color temperature about 1,800 to 2,000 K, daylight about 5,500 to 6,500 K: Wikipedia "Color temperature" (table of sources: candle flame 1,850 K), and Rosco and Lee filter guides for CTO and CTB.
- Oslo late December day length and sunset: computed (NOAA solar position equations) for 59.91 N, 10.75 E on 26 December: sunrise 9:19, sunset 15:15 CET, day length 5.9 hours.
- Gel names: Rosco Roscolux swatchbook (R02 Bastard Amber, R26 Light Red, R33 No Color Pink, R60 No Color Blue, R80 Primary Blue), Lee Filters (201 Full C.T. Blue, 204 Full C.T. Orange). Display colors, warmth scores and transmissions are this tool's approximations and say so.
- Instrument beam angles (ERS 19° and 36°, Fresnel spot to flood, PAR oval): ETC Source Four and typical Fresnel and PAR64 data sheets; the Φ values are the model's own units.
- Number checks (Python, 2026-10-29): throws and pools: FOH ERS 19° at (0, -6, 8) to the table (0, 3.4, 1.6): throw 11.37 m, pool 3.80 m, E 0.88, shown 0.59; 1st electric ERS 36° to Nora's chair: throw 5.26 m, pool 3.42 m, E 1.09, shown 0.66; 1st electric Fresnel flood: pool 4.90 m, E 0.53, shown 0.41; Fresnel spot: pool 1.85 m, E 3.72, shown 0.98 (a hot spot); 2nd electric PAR straight down: oval 1.06 by 2.50 m, shown 1.0. So FOH, electrics and booms all land in a useful range. Sun: 5.92 hours of daylight. Contrast ratios in Look computed.

## Done when
1. Focus: the plan in Hang, the board and cue list in Cues, and the Run view with its graph in Run are the largest things on screen at 1366 x 768 and 680 x 425.
2. Hanging, aiming and the throw and pool readouts match the numbers in Sources for those five setups.
3. The Run view relights the painted set so a pool lands where its ring is on the plan, and the actors' brightness follows the pools they stand in.
4. A design with cues only at beats 1 and 2 produces the observation about beat 5 and the noTurn line; adding cues at 5 and 8 produces allTurns.
5. While the scene runs, Stop, Step, Back and a scrubber tap act in the same frame, and a fader change shows on the next frame.
6. All channels at 0 shows the warning and the dark line; all at 100 never errors.
7. The design survives a reload; Clear design empties it.
8. How lines once each over five hangs in a row; noTurn, allTurns and dark every time their event happens.
9. The script text matches Project Gutenberg 2542 word for word except the dash substitutions.
10. All images load with no people and no lettering.
