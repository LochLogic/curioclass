# Play lens: levels-and-pathways (round 1)

Fresh, cold run on the CURIO_DRAFT=1 bundle (levels-and-pathways.html, 2026-11-04). Played twice: as a K-2 student alone
at home (taps only, listening to the narrator, reading nothing), and as a teacher projecting it at 1366x768 and 1920x1080.
Frames: the shared audit (audit-r1/) plus my own in the scratch folder
`scratchpad/refine/levels-and-pathways/play/frames/` (driven by play/run.py and run2.py with held clicks and real drags,
ports 9771/9772, own profiles). Every frame named below was looked at.

**Counts: blockers 0, should fix 5, polish 3, nit 2.**

## What works

- The first screen says what to do (hint and welcome name "Tap a move"), every mode's welcome names its control, and
  the hint moves on to the next action after each waiting moment: after a freeze it returns to the Levels how line
  (ms-late), after a trip to the Pathways how line (ms-pathlate), after a drawn path to "Now tap Dance it"
  (dr-zz-settled), after a right answer to "Tap Next" (my-solved). Read reads the current hint.
- Don't-nag holds: how lines go silent on repeat (Copy me, askPath after a replay), event lines speak every time
  ("Stretch!" 5 of 5 at a 2 s pace, st5 log).
- Mystery path gives nothing away: no ribbon, no level-guide glow and no spoken pathway or way during the trip
  (my-trip, my-r2trip); the ribbon painted in after a right path answer stays a neutral cream until the level is
  answered (audit state-mystery-level-question). Answer buttons dim while the dancer travels and during a replay
  (my-wrong).
- Draw a path reads real drags well: a jittery three-corner scribble is one zigzag (dr-zz-settled), a half-circle
  drag is one curved part (dr-arc), a 5-unit stub gets tooShort and its hint (dr-tiny). Part badges cycle levels and
  the ribbon changes per part (db-badge1, db-badge2).
- Pathways: the dotted preview of the chosen pathway before Go is a good teaching touch; a fourth trip clears the
  oldest ribbon and older ones fade (pa-t4end). Calm mode keeps the count timing (calm-mid at 9 s is on count 6, as
  with Motion on).
- The Ribbon gallery is a real payoff: eight ribbons in cells with their badges and a bow (gal-end).

## Findings

### Should fix

1. **Draw a path, four parts at small sizes: badge leader lines tangle across the drawing.** Mode Draw a path, the
   four-part drawn path at 680x425 and 375 wide. The four badges stack in a 2x2 block over the back of the floor and
   their black elbow leader lines run across the path and across each other (badge 1, the front straight part, sits
   over the back part; badge 4's leader runs under badge 3 and down the right side). A teacher on the tool-page preview,
   or a student on a phone, cannot tell which badge belongs to which part, and tapping a badge is how a part's level
   changes. At 1366x768 the same path puts each badge next to its part (audit state-four-part-drawn-path-1366x768).
   Seen: audit state-four-part-drawn-path-680x425.png and -375x812.png, zoomed in play/frames/z-375parts.png and
   z-680parts.png. Better: on small stages put each badge on or right beside its own part (a smaller badge over the
   floor near the part's midpoint), with short straight leaders that never cross another part. **family:dance**
   (part-badge placement in Draw a path).
2. **The painted dancer breaks apart in kneeling Low poses.** Mode Levels, Low level, Bend, Twist and Swing (kneeling
   back on the heels). The leggings end at the knee with orange skin-colored patches showing at both knee joints, the
   shins vanish so the legs read as stumps, and the elbows show jagged cut edges; in Low Swing the head sinks into the
   shoulders. On a projector the dancer looks broken, not kneeling (POLISH, Art: never crop a character mid-body, hard
   edges read as broken). Seen: lv-bendtolow.png (zoom z-bendlow.png), lowm-twist.png and lowm-swing.png (strip
   z-low-strip.png). The same cut-arm look shows, milder, on the Mystery dancer's shoulders while walking
   (z-mytrip.png). Better: a kneeling leg piece (thigh with the folded shin and foot behind) or a joint overlap so no
   gap shows, and a neck limit in Low Swing. **family:dance** (painted cutout figure on the dance pose engine).
3. **The level guide looks like three big buttons but does nothing.** Stage left, every mode. High, Middle and Low are
   tall rounded cards with borders, an icon and a word, the active one filled and pointed at: they look just like the
   level buttons in the panel and are the biggest targets on screen. A K-2 child alone taps Low there and nothing
   happens (the tap only plays the welcome). Seen: guide run, a held tap at (60, 225) left the level on middle;
   frame guide-tapguide.png. Better: make each band set the level (same as the panel button), or restyle it so it no
   longer looks like a control (no card border, one scale strip). **general** (a display that looks like a control).
4. **The end of Mystery path does not say how to go on.** Mode Mystery path after round 8, the Ribbon gallery. The hint
   and line are "Eight mysteries solved! Look at all our ribbons." and Play again is the only control; nothing names
   it, so a non-reader alone is left at a still screen (STANDARDS, Say how to act). Seen: gal-end.png, gal-end680.png,
   gal-end760.png; hint text in the gal log. Better: after the bow, the hint (and a once-only how line) says "Tap Play
   again for new mysteries." **general**.
5. **The Mystery hint names a dimmed control during the trip.** Mode Mystery path, after Go, while the dancer travels
   (16 counts, more than 10 s). The hint still reads "The magic floor hides the pathway. Tap Go, watch the dancer, then
   draw the pathway in the air with one finger." while Go is dimmed; the same in round 2 (STANDARDS: the hint changes
   when the state changes; no line names a disabled control). Seen: my-trip.png, my-r2trip.png. Better: on Go the hint
   becomes the watching step, for example "Watch the dancer. Draw the pathway in the air with your finger."
   **general**.

### Polish

6. **"Middle level. Stay in the middle." is unclear for K-2.** Levels, Pathways and Draw a path, the atMiddle line. To
   a five-year-old "stay in the middle" means the middle of the room, not a body height, and it is the line heard most
   (Middle is the default level). High and Low each name a body action ("Reach up to the sky", "Get close to the
   floor"). Better: a body cue such as "Middle level. Stand up, not too high and not too low." Seen: lv and ud logs
   (spoken on every Middle move and every Middle step of Up and down). **general** (needs a new clip).
7. **The first move takes about 8 s from tap to motion.** Levels, the first move on a fresh page: "Stretch!", the level
   line and "Copy me! Stay in your own bubble space." play in turn, then a 4-click count-in, and the dancer stands still
   in her idle pose the whole time (tap at 1.3 s, Copy me ends near 9 s; lv-countin.png and lv-mid.png show the same
   pose). Middle Stretch also starts from almost the idle pose, so the first move a class sees barely changes
   (z-ms-strip.png). For K-2 this first wait is where attention drops. Better: fold Copy me into the Levels welcome so
   the first move has two short calls, not three, or let the dancer take the move's first shape as the call ends.
   **general**.
8. **The gallery star covers a ribbon.** Mystery path, Ribbon gallery: the start star sits on the left end of the
   fifth ribbon (curved, high), hiding its first prints at 1366x768 and 680x425. Better: hide the star in the gallery or
   move the second row right. Seen: gal-end.png, gal-end680.png. **family:dance** (gallery layout).

### Nit

9. **A ribbon's end badge touches the dancer.** Pathways, a Low trip that ends at the right: the pathway badge at the
   ribbon's end sits on the crouched dancer's arm (audit state-ribbon-finished-1366x768, pa-t4end.png).
   **family:dance**.
10. **760x900 leaves the stage short.** In Draw a path at 760x900 the stage is about 225 px tall with about 120 px of
    empty space under the panel (db-n760.png); drawing in that strip is cramped. Let the stage take the spare height.
    **general**.

## Not findings (checked)

- Low Shake is a lying-on-the-back shake with legs and arms up (z-shake-strip.png): it reads as a real low shape, not a
  fall, and the reflection matches. The spec's Content table still says "crouching"; that is for the Teaching lens.
- The low slide (a wide squat, arms out) and the low walk end pose read as low, and the mirror matches (z-slide.png).
- Mirror reflections matched the dancer in every frame I checked.
- Pathways: after a trip the hint moves from the ribbon line to the Pathways how line once the line ends (about 3 s);
  frames taken sooner show the ribbon line, which is right for that moment.

## Audit pilot

Leads confirmed:
- Welcome "not heard" after a first tap on a level or move button: true, but by design and not a finding. A first tap
  on High speaks the level, then the short how "Tap a move, and copy the dancer!" (first-high log); a first tap on
  Stretch brings the full welcome back right after the freeze (lv log, 17.5 s). The student is never left without the
  next action.
- Its clean rows for sizes and states (overlap, fold, targets) held in every frame I re-shot.

Leads that were wrong:
- "#d-surprise left disabled after a resize mid-action": not reproduced. Surprise path, then 1366 to 760x900 and back
  mid-narration: no control or part badge is aria-disabled afterwards, the same as the plain run (rs and plain logs).
  The source never disables d-surprise.
- "Stretch: event line lost, spoken 0 of 5": wrong. Five held taps 2 s apart spoke "Stretch!" five times (st5 log); the
  "dropped, stale" rows it counted are the tool's blank stopper entries (an empty V.say with valid false).

What it missed:
- The leader-line tangle in Draw a path at 680x425 and 375 (finding 1): its "lines drawn across labels" check passed
  because the lines cross the drawn path and each other, not a label.
- The painted-figure seams in kneeling poses (finding 2), the level guide that looks like buttons (finding 3), the
  gallery end with no next action (finding 4) and the hint naming a dimmed Go during a Mystery trip (finding 5): none
  are in its states or checks.
