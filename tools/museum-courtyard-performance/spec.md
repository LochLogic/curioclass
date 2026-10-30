# Museum Courtyard Performance

## One idea
The courtyard rewrites your dance: columns block some seats, the fountain is loud and wets the stone, the stone is hard on landings and half the audience looks down from a balcony; over six weeks you decide which features to fight and which to use, on a budget and without wearing out your dancers, and opening night shows what the ground seats and the balcony each actually saw and heard.

## Not like
- choreography-for-a-cause (this band): makes and revises the dance itself from research. Here the dance is given; you adapt and produce it in a place.
- recital-practice-plan (this band, tycoon): practice minutes and listening. Here the currencies are money, crew hours and the dancers' bodies, and the result is sightlines and sound.
- mini-documentary-crew (this band, tycoon): schedules shoots and cuts a film. Here the work happens in one physical space you plan from above.
- stage-blocker and director-s-chair (stage family): seats and sightlines on theater stages. Here there is no stage: the site's architecture is the set, and the choices are production choices (floors, sound, light, safety, rehearsal time).
- dancers-on-tour (6-8, this batch): travel between venues. Here one site, studied closely.

## Who and how
- Grade 9-12, dance, module "Site-Specific Performance (Dance)".
- Topic line: producing a dance in an unusual venue
- Driver: students on laptops, alone or in pairs. 30 to 45 minutes for a full six weeks; saved on this device.
- Standards: NCAS DA:Pr4 (adapt movement to a space), DA:Pr5 (healthy practices and safe rehearsal), DA:Pr6 (production elements and presenting in a venue).

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound`. Own light palette (Look). Modes (`.seg`): `Site` (default), `Week`, `Opening night`. Opening night opens after week 6.

**Site.** Focus: the courtyard plan (top view, code over painted textures), filling the stage. The plan shows the stone floor, two arcades of four columns each, the fountain, the ground seating (three rows of 20) and the balcony along the north wall (40 seats; the 3 m under it shaded as "under the balcony"). The piece's four sections (Content) are colored ellipses (6 m by 4 m) you drag anywhere on the floor; a section selected shows its readouts live: "Seen from the ground 79%", "Seen from the balcony 100%", warnings in words ("Within 1 m of the fountain: wet stone while it runs"). Panel: the selected section's card (name, length, what it does) and its adaptation choices (Content), `Fountain` (`Running`, `Off for the show` once permission is granted, `Part of the score` once recorded), and the budget, crew-hours and week readouts. A `Seat view` toggle shows a corner inset (one third of the stage) from a chosen seat (tap any seat dot): a simple 3D view drawn in code with painted textures (Art), dancers as small figures in their section's zone.

**Week.** Focus: the production meeting board: this week's action cards in a row, large, with the plan small beside them. Week tabs 1 to 6 (only the current and earlier are open). Twelve action cards (Content) show cost, crew hours and what they do; tap to add to the week (up to 10 crew hours a week; the budget can't go below $0; one-time cards gray out once used). `Site rehearsal` asks which two sections to rehearse on site and whether Rise does `Full jumps`, `Half jumps` or `Mark the jumps`. `End week` applies the cards, runs the week's model (Interactions) and shows the week report: money left, hours used, sections adapted (dots per section, 2 needed), the dancers' load bar for the week (with the 120 line), and any event (Content). `Undo week` is allowed until the next week ends.

**Opening night.** Focus: the courtyard, wide, with two seat views (ground seat and balcony seat) side by side under it. `Begin` plays the piece compressed: each section 10 s (40 s; it is the show), dancers moving in their zones in the plan and both seat views, music as a Web Audio score with the fountain as a noise layer when running. `Stop`, `Skip section`, and seat taps on the plan (change the ground or balcony seat at once, mid-show). Then the program sheet: per audience (ground, balcony) Seen, Heard and Lit percentages for each section; the balcony line "Floor patterns read from above: yes" for sections whose pathway is visible from the balcony; site use (which of fountain, columns and balcony the piece used, Content); dancers (any sore weeks, any injury); money and crew hours left. `Print sheet`, `Start over` (confirm).

## Content
**The piece**: "Water Over Stone", an original dance for Curio Class, 6 minutes, 6 dancers, in four 90-second sections:
- S1 Arrival: a procession that travels in a straight line from one arcade across the courtyard. Level middle, 0 jumps. Choice: `Enter from the west arcade` / `Enter from the east arcade`.
- S2 Pool: floor work, rolling and sliding at low level. Choice: `Floor work` (low) / `Kneeling and sitting` (low, easier to see) / `Standing version` (middle; loses the slide).
- S3 Columns: weaving in and out between columns. Choice: `In an arcade` (the zone must overlap an arcade) / `Open floor` (no columns to weave).
- S4 Rise: the finale, 24 jumps and two lifts. Choice on the night: `Full jumps` (24) / `Half jumps` (12). (Marking is for rehearsal only.)

**The courtyard** (plan meters; x 0 to 20 west to east, y 0 to 16 south to north): columns radius 0.3 m at x 3 and x 17, y 4, 7, 10, 13; fountain basin center (10, 10), spray radius 1.5 m when running; ground seats 3 rows of 20 at y 0.6, 1.5, 2.4 (eye 1.2 m), x 1 to 19; balcony at y 16, floor 5 m up, sees nothing north of y 13. Museum rules (a made-up museum, said on screen): on-site rehearsals only on Mondays (the museum is closed); the show starts 30 minutes before sunset, so S3 and S4 happen after dusk.

**Action cards** (cost; crew hours; effect):
1. Marley floor 8 x 8 m ($900; 4 h; once): a vinyl dance floor over the stone, placed as a square on the plan; landings on it count as marley. Not allowed within 1 m of the running fountain.
2. Sprung floor panels 6 x 6 m ($1,800; 6 h; once): a raised floor that gives under landings; landings count as sprung.
3. Risers for ground rows 2 and 3 ($600; 4 h; once): low-level sections seen 90% instead of 50% from those rows.
4. Sound system, two speakers ($500; 3 h; once): music heard better (table below).
5. Record the fountain ($0; 3 h; once): the sound designer builds the score around the fountain; unlocks `Part of the score`.
6. Ask to turn off the fountain ($0; 1 h; once): the museum agrees for the show only; unlocks `Off for the show`.
7. LED wash lights ($700; 4 h; once): S3 and S4 lit 100% instead of 40%.
8. Column uplights ($400; 3 h; once): S3 in an arcade seen 10 points more from both audiences after dusk (cap 100%); counts as using the columns at night.
9. Site rehearsal ($150 guard overtime; 2 h; once a week): rehearse two sections on site; each gets an adaptation dot.
10. Warm-up and cool-down plan ($0; 1 h; once): every later week's load x 0.8.
11. Balcony safety: ushers and a railing check ($200; 2 h; once): without it the museum limits the balcony to 20 seats.
12. Rain backup in the lobby ($300; 2 h; once): if it rains on a site rehearsal, it moves to the lobby and rehearses one section instead of none.
- Starting budget $3,000; crew 10 hours a week. Event: in week 6 it rains on Monday (the forecast shows "rain Monday" from week 5).

**Model** (a `How the model works` note, "a simple model, not a law"):
- Seen from the ground = mean over the 60 seats of the share of the section's zone not hidden by a column (or by the fountain spray when running), times the low-level factor (row 1 sees floor work fully; rows 2 and 3 see it 50%, or 90% with risers; Kneeling and sitting counts 75%), times light (S3 and S4: 40% without LED wash), times 0.85 if the section has fewer than 2 adaptation dots ("spacing slips").
- Seen from the balcony = the share of the zone at y 13 or less (outside the overhang), times light, times the same spacing factor.
- Heard (ground, balcony): fountain running without the sound system 70%, 45%; with it 95%, 90%; off for the show 90%, 80% without, 100%, 100% with; part of the score 90%, 85% without, 100%, 95% with.
- Floor patterns read from above: S1, S2 and S3 when the balcony sees 70% or more of them.
- Dancers' load each week = jumps rehearsed on site x 3 runs x floor (stone 3, marley 2, sprung 1) x 0.8 with the warm-up plan; studio rehearsals on a sprung floor are not counted. Over 120 is a sore week; two sore weeks in a row injure a dancer, and Rise is danced by 5 (the sheet says so). Marking the jumps counts as 0.3 of the jumps.
- Wet stone: a section zone within 1 m of the basin edge while the fountain runs is flagged "slip risk" on the plan and the sheet.
- Site use: fountain (recorded into the score, or S2 within 3 m of a fountain that is off: "dancing by the still pool"), columns (S3 in an arcade), balcony (at least two sections with floor patterns read from above).

## Interactions in detail
- Readouts update live while dragging a zone (sampled on a 9 by 9 grid inside the ellipse, 60 seats, rays against columns and spray), throttled to one recompute per animation frame.
- A zone can't leave the floor, cover the fountain basin or overlap the seats; it slides along the edge instead.
- Week rules: crew hours never pass 10 (a card that won't fit shows "Needs 4 h, 2 h left"); money never goes below $0; one-time cards gray out with "Done in week 2".
- `End week` with no cards is allowed ("A quiet week").
- Extremes: placing S3 deep in the west arcade with no uplights or LED wash gives ground Seen about 79% x 40% = 32% after dusk, and the sheet says why in words. Six site weeks of full jumps on stone (216 a week) injure a dancer by week 2.
- Opening night uses the final week's state; changing the plan in Site after week 6 asks "Change the plan for the show?" and allows only zone moves and choices (no new cards).
- Saving: localStorage `curio-museum-courtyard`. `Start over` clears all.
- Sizes: at 1366 x 768 the plan and the panel fit without scrolling; at 680 x 425 the Seat view inset is hidden behind a `Seat view` toggle that swaps it with the plan; at 375 wide the action cards scroll sideways with `End week` pinned.

## Look
- Own light palette (limestone in late sun): paper #f3efe6, panel #fbf9f4, ink #23211c, muted #5f5a4e, line #d8d0bf; accent (`--brand`) #4d6b14 boxwood green. Section colors (fill at 35%, outline solid, each with its number): S1 #b45309, S2 #1d4ed8, S3 #7e22ce, S4 #be123c. Warnings #9a3412 with a triangle icon.
- Contrast (computed in Python): brand on paper 5.34:1; white on brand 6.12:1; ink on paper 14.01:1; muted on paper 5.98:1.
- Different from every 9-12 arts neighbor (virtual-gallery lime on dark, brand-builder green on white is #047857, a cooler and darker green) and every other spec in this band.

## Art
Local FLUX, no people, no lettering. 9 images, none for Gemini. webp.
- mcp-hero: a painting of a stone museum courtyard at golden hour, two arcades of pale columns, a round fountain in the middle, a balcony along the far wall, empty; 16:9; cutout no; people no; Opening night backdrop at the top and the program sheet header.
- mcp-stone: a seamless top-down texture of pale limestone paving slabs, soft even light, filling the frame; 1:1; no; no; tiled on the plan floor and the seat-view floor.
- mcp-column: a painting of a single pale stone column with a simple capital, front view, on a plain dark background; 9:16; cutout yes; no; drawn at each column's place in the seat views, scaled by distance.
- mcp-fountain: a painting of a round stone fountain basin with a central spout, front view, water spraying, on a plain dark background; 1:1; cutout yes; no; seat views when running (a second state, mcp-fountain-still, shows still water).
- mcp-fountain-still: the same round stone fountain basin, front view, still water, no spray, on a plain dark background; 1:1; cutout yes; no; seat views when off.
- mcp-marley: a painting of a rolled gray vinyl dance floor and a roll of tape on stone; 1:1; cutout yes; no; card 1.
- mcp-speaker: a painting of a black portable speaker on a tripod stand; 1:1; cutout yes; no; card 4.
- mcp-uplight: a painting of a small LED uplight fixture on the ground casting a warm beam up a stone column at dusk; 1:1; no; no; card 8.
- mcp-risers: a painting of folding audience risers with a row of empty chairs; 1:1; cutout yes; no; card 3.
- Drawn in code: the plan (columns, basin, seats, balcony line, zones, rays), the seat views' geometry (the textures and cutouts placed by the plan's coordinates so sightlines match the numbers), dancers (the dance engine's figure, small, no faces), cards' text and the sheet.

## Voice
Bank voice: `knowing-guide` (Sadaltager), "Say in a knowledgeable, friendly way, like a museum curator", here the museum's events curator hosting your show. Not used by any 9-12 arts neighbor (dance-styles-explorer and brand-builder moved off it) or another spec in this band. `Curio.voice`, scope = mode.
- welcomeSite (how; Site entered; stale once a zone is dragged): "Drag a section onto the courtyard floor and watch what each audience can see."
- seatHow (how; the first zone moved; stale once Seat view is opened): "Tap Seat view, then tap any seat to sit there."
- welcomeWeek (how; Week entered; stale once a card is added): "Tap action cards for this week, then tap End week."
- sore (event; each week ending over the load line; stale when the week tab changes): "Your dancers are sore this week. Their landings were too hard."
- injured (event; when an injury happens; stale when the week tab changes): "A dancer is hurt. Rise goes on with five."
- rain (event; week 6 ends with the rain; stale when the week tab changes): "Rain on Monday. The courtyard was closed for rehearsal."
- welcomeNight (how; Opening night entered; stale once Begin is tapped): "Tap Begin. Tap any seat on the plan to watch from there."
- siteAll (event; a sheet where the piece used all three features; stale when the mode changes): "You used the fountain, the columns and the balcony. The courtyard became part of the dance."

## Family engine
Uses `kit/dance.js` (docs/families/dance.md) for the dancer figure and poses only (`Dance.dancer` in the seat views, `Dance.poses` and a short `Dance.phrase` per section so the figures move in the right level: S2 low, S4 jumps with `lift`), with the engine's one-run-at-a-time rule. The catalog lists no family for this tool; the courtyard, model and plan are the tool's own.

## Sources
- NCAS Dance DA:Pr4, DA:Pr5, DA:Pr6: https://www.nationalartsstandards.org/
- Floors and dancer health (hard surfaces such as concrete and stone raise impact on landings; sprung floors absorb it; vinyl dance flooring over a hard floor gives grip, not cushioning; warm-up and cool-down as safe practice): Quin, E., Rafferty, S. and Tomlinson, C., Safe Dance Practice (Human Kinetics, 2015), chapters on the dance environment and warm-up; International Association for Dance Medicine and Science, resource paper "Dance Floors" (https://iadms.org/resources/).
- Site-specific dance as a form: Kloetzel, M. and Pavlik, C. (eds.), Site Dance: Choreographers and the Lure of Alternative Spaces (University Press of Florida, 2009).
- The museum, piece, prices and every model number are made up for this tool and say so on screen.
- Number checks (Python, 2026-10-29): ground-seat sightlines (60 seats, 9 x 9 zone samples, columns radius 0.3 m): zone centered (10, 6) 100%, (10, 8) 98%, either arcade (3, 8.5) or (17, 8.5) 79%; behind the fountain at (10, 13) 37% with spray, 92% without. Balcony: zones south of y 11 100%, (10, 13) 59%, (10, 14) 27%. Budget: every card once plus six site rehearsals costs $6,300 and 45 crew hours, so $3,000 forces choices; a sample plan (marley, sound, LED, balcony safety, record, warm-up, 4 site rehearsals) costs $2,900 and 25 hours. Load per site week (3 runs): 24 jumps on stone 216, with warm-up 173; 12 on stone 108; 24 on marley 144, with warm-up 115; 24 on sprung 72. So the 120 line catches full jumps on stone or marley without a warm-up. Contrast ratios in Look computed.

## Done when
1. Focus: the plan in Site, the action cards in Week and the courtyard with both seat views on Opening night are the biggest things on screen at 1366 x 768 and 680 x 425.
2. Dragging zones reproduces the sightline numbers in Sources to within 2 points.
3. Crew hours and budget limits hold; one-time cards gray out; Undo week restores the week before.
4. Full jumps on stone in two site weeks in a row injure a dancer, and the sheet and the injured line say so; the warm-up plan changes the loads as in Sources.
5. The week 6 rain cancels the site rehearsal unless the backup was booked (then one section gets a dot).
6. During the opening night run, Stop, Skip section and seat taps act in the same frame; the run lasts about 40 s.
7. The program sheet's numbers match the model for a sample plan worked by hand.
8. How lines once each in five weeks; sore, injured, rain and siteAll every time their event happens.
9. All 9 images load with no people and no lettering.
