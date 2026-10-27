# Stage Blocker

## One idea
Block a scene from above, then sit in any seat in the house: the audience view shows what that seat really sees on every line, who is hidden behind whom, who is upstaging whom, and where the eye goes, and the director's notes check it from all sixteen seats at once.

## Not like
- choreography-board (6-8, dance group): builds a dance on a timeline of phrases shown in a side view. Here it is a script with lines, top-down blocking and seats in a house, and the test is sightlines and focus, not counts and formations.
- design-fixer (6-8, puzzle): moves poster parts until the eye lands right on a flat page. Here the eye problem is three-dimensional: the same blocking reads differently from house left, house right and the balcony.
- frame-it (6-8, lab): moves a camera over a fixed scene. Here the seats are fixed and the actors and set move.
- vanishing-point-studio (6-8, studio): draws perspective. Here the perspective is computed for you; the work is placement.
- director-s-chair (9-12, same family): five historical stage shapes and their rules, one classic scene, choices in a story. Here it is one modern proscenium, original scenes, and free placement you test against notes.
- character-voice-booth (3-5, same group): voice only.

## Who and how
- Grade 6-8, theater, module "Scripts and Staging (Theater)": blocking, stage directions and design.
- Topic line: blocking, stage directions and sightlines
- Driver: students on laptops, alone or in pairs (a director and a stage manager); or a teacher on a projector blocking a scene with the class. 30 to 45 minutes.
- Standards: NCAS TH:Cr1 (generate and conceptualize ideas: design and staging choices), TH:Pr5 (develop and refine work for presentation: blocking and technical elements).

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound` (kit). Mode buttons (`.seg`): `Block` (default), `House`, `Run`. Panel top: `Scene` picker (The Note, Bus Stop, The Trophy, Free stage).

**Block.** The stage is the ground plan, top-down, drawn at real pixel size: a black stage floor, the proscenium line and apron at the bottom, the house (16 seat dots) below it, wings left and right, entrances marked with arrows and names. The nine areas are outlined faintly with labels in the actor's view (USR, USC, USL, CSR, CS, CSL, DSR, DSC, DSL; `Show areas` toggles them). A small live seat view (the House view from the chosen seat) sits in the top corner of the stage.
- Panel: the Beat list (number, speaker, line, and a status icon for each director's note on that beat: check, cross, or dot when not yet checked). Tap a beat to make it current; the plan shows that beat. `Prev beat`, `Next beat`.
- Cast tokens: a colored disc with initials and a nose wedge for facing, dragged from the wing shelf onto the stage. Selected actor tools: `Turn left` and `Turn right` (45 degrees), `Face partner` (turns to face the beat's "to" actor), `Stand` / `Sit` / `Kneel`, `Off stage`.
- Set shelf: table, chair, bench, sofa, door flat, platform, tree, crate, lamp post. Drag onto the stage; selected piece: `Rotate` (90 degrees), `Remove`. Actors dropped on a platform stand on it.
- Lights: a 3 by 3 grid of area buttons (each cycles off, half, full, shown as an icon and a word) and `Spot` (one special, dragged onto the plan). Pools are drawn on the floor.
- Toggles: `Sightlines` (rays from the chosen seat to each actor's face, solid where clear, red and dashed where blocked), `Focus` (bars per actor, Content "Focus"). Seat picker: tap a seat dot on the plan or use `Seat` (cycles).
- Crosses: when an actor's place differs from the previous beat, an arrow shows the cross.

**House.** The seat view fills the stage, drawn in perspective from the chosen seat: the proscenium frame, the stage floor, set pieces as solid shapes, actors as simple figures (rounded body, head, the actor's color and initials on the chest). Hidden actors get an outline "ghost" and the word "hidden"; partly hidden ones "partly hidden". Each visible actor carries a small body position tag from that seat ("full front", "one-quarter", "profile", "three-quarter", "full back"). An eye icon marks the focus leader. The ground plan shrinks to the corner with the seat map, so seats are picked in either mode. `Prev beat` / `Next beat`, and the line as a caption.

**Run.** Plays the whole scene in the House view from the chosen seat: each beat's line as a caption, crosses tweening (1.2 s each; Motion off: jumps), light changes fading (400 ms; Motion off: cuts), a cue tag in the corner ("Cue 4: GO"). Then every director's note is checked from all sixteen seats and listed: met (check and words) or not met (cross and why, for example "Ben covers Ava from seats A1, A2, B1"). Tap a note to jump to its beat in Block. `Run again`, `Stop`.

**Free stage.** An empty stage with six actor tokens (names editable, 1 to 12 letters; initials from them), up to 12 beats (speaker, "to", a line up to 120 characters). No director's notes; every analysis still works. `Save on this device` and `Clear` (localStorage `curio-stage-blocker`).

## Content
**The stage** (the engine's `proscenium` house; sizes are this tool's own choice, typical of a school stage): opening 10 m wide, playing area 7 m deep, apron 1 m in front of the curtain line, stage floor 0.9 m above the house floor. Areas: three columns and three rows of equal size. Entrances: `SR wing` and `SL wing` (at y = 1, 3.5 and 6 m), `Door` (when a door flat is set). Seats: rows A, B, C at 3, 6 and 9 m from the apron, seats 1 to 5 at x = -6, -3, 0, 3, 6 m (seat 1 is house left), eye height 1.1 m plus a 0.3 m rake per row; `Balcony` center at 12 m, eye 5 m. 16 seats.

**Set pieces** (w by d by h, m): table 1.2x0.8x0.75; chair 0.5x0.5x0.9; bench 1.6x0.45x0.45; sofa 2.0x0.9x0.85; door flat 2.0x0.1x2.4 (opening 0.9 wide in the middle, an entrance); platform 2.0x1.5x0.6 (standable); tree 1.0 round, trunk 0.3 wide to 1.8, canopy 1.8 to 3.0; crate 0.6x0.6x0.6; lamp post 0.2x0.2x3.0.

**Scenes** (original, written for this tool). Each beat: speaker (to), line; notes.
*The Note* (Ava, Ben, Gran; set: table, two chairs, door flat upstage center). Starts with Ava seated at the table.
1. Ava: "'Meet me at the old oak at midnight.' Who wrote this?" Notes: Ava can be seen from every seat; Ava is lit.
2. Ben enters by the Door. Ben (Ava): "Have you seen my notebook?" Notes: Ben enters by the Door; Ben does not hide Ava from any seat.
3. Ava (Ben): "What notebook?" Notes: Ava is not upstaged.
4. Ben (Ava): "The blue one. I left a page in it." Notes: Ben crosses at least 1.5 m.
5. Gran enters SL. Gran (Ava): "Ben. Ava. Who left the back door open?" Notes: Gran has the focus.
6. Ava (Gran): "It was the wind, Gran." Notes: Ava and Ben at least 2 m apart.
7. Ben exits SR. Ava: "The old oak. Tonight." Notes: Ben exits SR; Ava has the focus; Ava is in a downstage area.
*Bus Stop* (Maya, Leo, Sam; set: bench, lamp post).
1. Maya: "Twenty minutes late. Again." Notes: Maya is in a downstage or center area; Maya is lit.
2. Leo enters SR. Leo (Maya): "Is this the stop for Elm Street?" Notes: Leo enters SR; Leo has the focus.
3. Maya (Leo): "If the bus ever comes." Notes: Maya is not upstaged.
4. Sam enters SL. Sam (Leo): "You can share my umbrella." Notes: Sam is lit; Sam is at least 2 m from Maya and from Leo.
5. Leo (Maya): "Do you know her?" Notes: Leo and Maya within 1.2 m; Sam hides neither from any seat.
6. Maya (Sam): "Fine. Just until the bus comes." Notes: all three within 1.5 m of each other; all three seen from every seat; the group in a center area.
*The Trophy* (Coach, Jordan, Riley, Priya; set: platform, crate).
1. Coach (all): "This year's most improved player is..." Notes: Coach is on the platform; Coach has the focus.
2. Riley (Jordan): "It's going to be you." Notes: Jordan, Riley and Priya are seen from every seat; none is full back from seat A3.
3. Coach (Riley): "...Riley!" Notes: Riley has the focus.
4. Riley crosses toward the platform. Riley (Coach): "Me? Really?" Notes: Riley crosses at least 2 m; Riley is not upstaged.
5. Jordan (Priya): "I thought it would be me." Notes: Jordan and Priya within 1.2 m; Jordan is in a downstage area; Jordan has the focus.
6. Riley (all): "This is for all of us." Notes: Riley has the focus; the crate is seen from every seat.

**Focus** (the "where the eye goes" model; weights are this tool's own, a rough model of common directing rules from Dean and Carra, shown as "a rough guide"): speaking +3; light full +2, half +1, off -3, spot +2 more; body position from the seat: full front +2, one-quarter +1.5, profile +1, three-quarter 0, full back -1; on a platform +1; standing while every other actor sits or kneels +1; downstage row +1, center row +0.5; crossed this beat +1.5; +1 for each other actor facing within 30 degrees of them; no other actor within 1.5 m +1; partly hidden -2; hidden: no score, "hidden". "Has the focus" in a note means the highest score from seats A3, B3 and C3.

## Interactions in detail
- Coordinates in meters: x from house left to house right (x = 0 at center; stage right is negative x), y upstage from the apron edge. Actor facing in degrees, 0 = toward seat B3. Arrow keys move a selected token 0.25 m; Q and E turn it 45 degrees.
- Beats carry forward: each beat starts as a copy of the previous beat; a beat you changed keeps its own layout; changing an earlier beat updates later beats only where they were never changed (a dot on the beat list marks changed beats).
- Entrances and exits: an actor whose first beat is later starts in its wing or behind the Door; "enters by X" is met when the actor is off stage in the previous beat and on stage now, and its nearest entrance is X. An actor can't be dropped inside a set piece (it slides to the nearest free spot).
- Sightlines: five points on the face (head center, 0.1 m left, right, up, down; head center 1.6 m standing, 1.2 sitting, 0.9 kneeling, plus 0.6 on a platform). A point is blocked when the ray from the seat's eye passes through another actor (a 0.25 m radius cylinder up to head top), a set piece box, or the proscenium wall beside the opening. 3 or more blocked: hidden; 1 or 2: partly hidden (this tool's thresholds). A prop is seen when its top center is unblocked.
- Body position: the angle between the actor's facing and the direction to the seat: under 22.5 full front, to 67.5 one-quarter, to 112.5 profile, to 157.5 three-quarter, above full back.
- Upstaged: the speaker's "to" partner stands at least 1 m farther upstage and the speaker, facing the partner, is three-quarter or full back from seat B3. The Run note says how to fix it: "Bring Ben down level with Ava, or have Ava cheat out."
- Notes are checked live in Block for the current beat (icons update) and all together in Run.
- Changing scene asks "Leave this scene? Your blocking here is kept until you close the page." Scenes keep their blocking in memory per scene.

## Look
- Accent (`--brand`) #9a4208 spike-tape orange. Paper (panel) #f7f4ef, ink #22201d, muted #5f5a52; stage floor #1b1b1f with area lines #3a3a42 and spike marks in accent tint #e07a2e; house #2a2a30 with seats as #8a8a94 dots; light pools warm #ffe7b0 at 20 to 35% over the floor.
- Actor colors on the floor, each with initials in ink #111114: #ff8a5c, #5ec8ff, #ffd84d, #7ee08a, #d9a3ff, #ff8fc6.
- Contrast: white on brand 6.7:1; brand on paper 6.1:1; ink on paper 14.8:1; muted on paper 6.2:1; spike orange on floor 5.7:1; actor colors on floor 7.4 to 12.4:1; initials on actor colors 8.1 to 13.6:1; panel paper text on floor 15.6:1.
- Different from the 6-8 arts neighbors: design-fixer #4338ca, art-through-time #8a2a2b, frame-it #ffb347, vanishing-point-studio charcoal and red.

## Art
none: drawn in code (ground plan, seat view, figures, set pieces).

## Voice
Bank voice `firm-captain` (Alnilam), style "Say firmly but kindly, like a ship captain giving clear directions": the stage manager. Not used by any 6-8 arts neighbor (design-fixer big-sister, art-through-time upbeat-guide) or this group. `Curio.voice` with `scope: () => state.mode + ':' + state.scene`.
- how, welcome (Block): "Drag the cast from the wings onto the stage. Then tap a seat to see what that seat sees."
- how, first actor placed: "Tap Next beat to block the next line."
- how, first upstaged flag: "Someone is upstaged. Bring the partner down, or turn the speaker out to the house."
- how, first hidden flag: "Someone is hidden from a seat. Move them, or move whoever is in the way."
- how, welcome (House): "This is what one seat sees. Tap another seat dot to sit somewhere else."
- how, welcome (Run): "Tap Run to watch the whole scene from your seat."
- event, Run start: "Places, please. House to half. Go."
- event, Run end: "Every note is met. That's a show." / "That's the run. Some notes need work. Tap a note to jump to its beat."
- event, a beat's notes all met in Block for the first time: "Notes met on this beat."
- Read speaks the hint, or in Run the current note list.

## Family engine
`kit/stage.js` (family stage: stage-blocker, director-s-chair). This spec holds the full description; director-s-chair says what it feeds. Loaded with `<script src="kit:stage"></script>` after the kit; exposes `Stage`. Colors come from CSS variables the tool sets. The builder also writes `docs/families/stage.md` from this section.
- `Stage.house(def)`: a stage shape. `{id, name, outline: polygon (m), areas: [{id, label, poly}], spots: {name: [x, y]}, entrances: [{id, label, at: [x, y]}], levels: [{id, poly, h}] (platforms, bridges), blockers: [{poly, h}] (proscenium walls, pillars), seats: [{id, label, x, y, eye}], frame: 'proscenium' | 'thrust' | 'arc' | 'open' (how the House view draws the surround), light: 'areas' | 'daylight' | 'even' (areas: the lights panel works; daylight and even: fixed full light, the lights panel shows why)}`. This tool defines `proscenium` (Content); director-s-chair adds five more.
- Cast: `{id, name, initials, color, mask: null | 'full' | 'half', x, y, facing, pose: 'stand' | 'sit' | 'kneel', on: level id or null, off: bool}`. Pieces: `{type, x, y, rot}` from a catalog `{w, d, h, standable, opening}`.
- Beats: `[{speaker, to, line, notes, snap: {cast, pieces, lights, spot}, changed}]` with the carry-forward rule above.
- `Stage.sight(snap, house, seat)` returns per actor `{blocked: 0..5, status: 'clear' | 'partly' | 'hidden', by: [ids]}` and per piece `{seen}`.
- `Stage.bodyPos(actor, seat)` returns one of the five positions (angles above).
- `Stage.focus(snap, beat, house, seat, weights)` returns per actor `{score, reasons: [text]}`; `weights` defaults to Content "Focus", and a house or tool may add terms (`chorusGaze`, `address`, used by director-s-chair).
- `Stage.upstaged(snap, beat, seat)` returns the speaker id or null, with the partner.
- `Stage.check(notes, beats, house)` returns per note `{met, why, seats}`. Note types: `see(actor)`, `lit(actor)`, `focus(actor)`, `at(actor, areas)`, `enters(actor, entrance)`, `exits(actor, entrance)`, `crosses(actor, m)`, `near(a, b, m)`, `apart(a, b, m)`, `notUpstaged(actor)`, `notHiding(a, b)`, `notFullBack(actor, seat)`, `onLevel(actor, level)`, `seeProp(piece)`, `group(ids, m, areas)`.
- Views: `Stage.view.plan(el, state, opts)` (top-down SVG at real pixel size, re-laid out on resize: drag and keyboard move, facing handle, area labels, cross arrows, light pools, seat dots, sightline rays; every actor shown by initials as well as color) and `Stage.view.house(el, state, seat, opts)` (canvas perspective from the seat, painter's order by distance, ghosts for hidden actors, position tags, focus eye, masks drawn as a face shape over the head when `mask` is set). `Stage.play(beats, view, {cross: 1200, fade: 400})` tweens between snapshots and returns a promise per beat; with `Curio.reduce` it jumps.
- This tool feeds: the `proscenium` house, the set catalog, three scenes with notes, and the default weights.

## Sources
- National Core Arts Standards, Theatre, grade 6 to 8 (TH:Cr1, TH:Pr5): https://www.nationalartsstandards.org
- Stage areas named from the actor's point of view (stage right is the actor's right facing the house), the five body positions, upstaging, and emphasis by position, level, light and movement: Alexander Dean and Lawrence Carra, Fundamentals of Play Directing, 5th ed. (Waveland Press, 1989), the chapters on composition and the body positions.
- Stage, set and seat sizes, sightline and focus thresholds and weights: this tool's own choices, labeled on screen as a rough guide.
- Scenes: original, written for this tool.

## Done when
1. The Note can be blocked so every note is met in Run, and the default start (Ben dropped straight upstage of Ava) fails "Ava is not upstaged" with the fix text.
2. Moving Ben between seat A1 and Ava hides Ava from A1 (and lists A1 in the why), while A5 still sees her; the House view from A1 shows Ava as a ghost.
3. Body position tags change correctly as an actor turns in 45 degree steps (check all five from seat B3 with Python).
4. Focus bars follow the weights: turning the speaker full back or turning their light off moves the eye icon to someone else.
5. Carry forward: moving Ava in beat 2 also moves her in beats 3 to 7 unless they were changed, and never in beat 1.
6. Run plays every beat with captions and cue tags, then lists every note with seat lists for failures; tapping a failed note opens its beat in Block.
7. Free stage saves and restores after reload, and Clear empties localStorage.
8. Drag works with whole-pixel jittered pointer input and with arrow keys; the panel controls come before the seat dots in tab order.
9. The plan, Prev beat and Next beat are visible without scrolling at 680x425, 1366x768 and 760 wide; text on the plan is 10 px or more in the preview.

