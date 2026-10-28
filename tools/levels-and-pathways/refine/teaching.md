# levels-and-pathways: Teaching lens (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json; bundled with `CURIO_DRAFT=1`; driven with
`scripts/drive.py` (port 9561, own profile). Scratch frames: `C:\Users\Cory\AppData\Local\Temp\claude\S--\98b8b046-f7f2-48d0-a719-c61ce01237be\scratchpad\lens-lp-teaching\r1`.
Standards text checked against the NCAS "Dance at a Glance" handout (nationalartsstandards.org, the source named in
data/standards/ncas-performance-standards.txt). Module arts-k-2-moving-bodies: DA:Cr1; DA:Pr4; DA:Re7; DA:Cr3; DA:Pr5;
SHAPE.S2. This is the module's only tool.

Counts: blockers 1 (general 0, family 1), should fix 3 (general 2, family 1), polish 5, nit 2.

## Blocker

1. **Draw a path calls a big zigzag "straight, straight, straight, straight".** src.html:731 (`ZIG_LEG = 40`) and
   analyze() 784-839. How I saw it: a real mouse drag from the star through (30,8), (50,50), (70,8), (90,50) in floor
   units, a deep full-floor zigzag, came back as 4 straight parts. The panel said "Then straight." and the stage showed 4
   numbered straight-line badges (frame `draw-deepzig.png`). With analyze() directly: a 3-leg zigzag across the floor
   (legs 43 to 48 units) came back "straight+straight+straight", and so did corners at (35,15), (60,50), (85,15). Smaller
   zigzags pass (legs 36 or less, the tool's own zigzag, a 5-leg one). On a projector a child's zigzag is most likely
   big and deep. The tool then tells the class that a zigzag is four straight pathways, which contradicts what Pathways
   and Mystery path just taught. The spec's own rule (legs under 30) is stricter still, so the rule itself needs
   fixing, not only the number. Better: two or more sharp corners in a row that **alternate turn direction** (left,
   right, left) make a zigzag at any leg length up to about 60 units. Corners that turn the same way (an L, a box)
   stay separate straight parts (`lThen` = straight+straight, still right). Tag: **family:dance** (the pathway
   classifier will come back in the dance siblings).

## Should fix

2. **Wrong code for Mystery path, and Re7 is not taught for grades 1 and 2.** spec.md "Who and how", src.html:10-11.
   How I saw it: the standards text. DA:Re7.1.Ka is "Find a movement that repeats in a dance." Mystery path
   (watch, then describe the pathway and level) teaches **DA:Re7.1.Kb** (demonstrate or describe observed or performed
   dance movements), and it teaches it well. Re7.1.1a and 2a (patterns) and Re7.1.1b and 2b (movements from a genre or
   culture) are not taught here, and this is the module's only tool, so DA:Re7 has no grade 1 or 2 coverage. Fix the
   citation to Re7.1.Kb. For grades 1 and 2, follow BASELINE rule 2 and the K-2 span rule (gf-04): send Re7.1.1a/2a to
   dance-pattern-puzzle and Re7.1.1b/2b to dance-styles-explorer, which teach those well, and don't add a thin activity
   here. Same kind of slip: the spec's text for DA:Cr1.1.Ka ("explore ... by changing an element") is the wording of
   **Cr1.1.Kb**. Kb is taught (every move at three levels), and Ka (respond in movement to stimuli: music, an observed
   dance) is taught by copying the dancer, so cite both. Tag: **general**.

3. **Draw a path doesn't teach the grade 1 and 2 Cr3 and Cr1 codes it claims.** spec.md cites DA:Cr3.1.Kb to 2b. How I
   saw it: the standards text against what the student does. Cr3.1.Kb (depict a movement by drawing or a symbol) is
   taught well: the child draws the pathway. Cr3.1.2b asks the child to "depict the levels of movements ... using
   symbols (for example, high, middle, low)", and Cr1.1.2b asks them to "combine a variety of movements while
   manipulating the elements of dance". In Draw a path, the drawing carries only the pathway. The level and the way
   are one button choice for the whole path, so the child never puts a level symbol into their map or combines
   movements. Cr3.1.1b (depict types of movement: jump, turn, slide, bend, reach) is not taught either. Better: let each
   drawn part carry its own level and way. Tap a part's number badge to cycle its level icon (cloud, table, grass),
   then Dance it changes level and way part by part. That teaches 2b of both anchors and gives grade 2 real depth.
   This changes the spec, so it goes to open questions. Until then, cite only Cr3.1.Kb. Tag: **general**.

4. **Some low-level freeze poses read as standing, not low.** src.html:216 (stretch low), 224 (bend low), 237 (curl
   low). How I saw it: each move posed at its count-8 hold (keyframe B) at each level, at 800x500 (frames
   `pose-*-*.png`, `grid-low.png`, `low-compare.png`). Low Curl's held pose is the "open" star lying on the floor.
   Seen from the front, the legs run toward the class, so it looks like a standing star whose head is nearly as high as
   the Middle figure. The class copies the freeze, so many children will stand in a star at "Low level". Low Stretch
   and Low Bend hold almost the same seated forward fold (lean 52 against 62, the same arms), so two moves look like
   one. The pose numbers differ (no duplicate among the 18), but Done when 1 asks for a shape of their own. Better: for
   floor poses, face the dancer about 60 degrees (side-ish) so the legs read as lying along the floor. Hold Low Curl on
   the small ball (keyframe A) at count 8, or end the loop on A. Make Low Bend a seated side bend. Tag:
   **family:dance** (Dance.level and the studio view decide how floor poses read; the handoff already lists "low ...
   can read as sitting").

## Polish

5. **"Stay in place" and "travel" are never named.** Cr1.1.Kb/1b and Pr5.1.Ka/1a/2a are about locomotor and
   non-locomotor movement, and the tool does both well (Levels in place, Pathways traveling), but the class never
   hears the difference. Better: wLevels "These moves stay in one place..." and wPaths "Now we travel!", plus a Talk
   about it prompt in notes.md: "Which moves stayed in your bubble? Which ones traveled?". Tag: general.
6. **Round 7's circle could teach Pr4.1.2a.** Pr4.1.2a asks children to "differentiate between circling and turning".
   Mystery round 7 (a full circle back to the star) is the natural moment. Add a notes prompt: "The dancer made a
   circle on the floor. Now turn around in your bubble. How is that different?". Tag: general.
7. **Cite DA:Pr5.1.2a.** It asks for dance sequences "moving through space using a variety of pathways", which
   Pathways and Draw a path teach directly. Add it to the spec's codes (it gives grade 2 a code the tool teaches
   fully). Tag: general.
8. **No inclusion note.** notes.md "Good to know" could add: a child who can't kneel, sit or go on tiptoe shows the
   level with the arms and the head (high reach, middle out, low near the lap), and a seated class can trace the
   pathway with a hand. Tag: general.
9. **The sides of a big curve get called straight.** analyze(): a drawn half-sine hump from the star (20 units high,
   80 wide) came back "straight+curved+straight". A child who drew one curve hears three parts. Better: split a straight
   end off a curve only when the curve's middle turns at least 90 degrees and the straight end is at least 30 units.
   Tag: family:dance.

## Nits

10. A drawing that doesn't start at the star gets an extra part 1 from the star (spec, Interactions). Then "First,
    straight." names a line the child didn't draw. A softer line would fit better ("From the star, ... then ...").
11. notes.md Mystery path: "A right pathway paints the ribbon in". It paints in gold first and takes the level's
    look only after the level answer. One more sentence helps the teacher see why.

## Checked and right

- **Facts recomputed (Python):**
  - Contrast: white on accent 5.10, accent on paper 4.79, ink on paper 14.43, muted on paper 6.04, ink on wood 10.55,
    and white on High, Middle and Low 5.75, 5.13 and 5.02. All match the spec.
  - Tempos: Walk 100, Skip 120, Gallop 120, Slide 100, Levels 96. Code matches the spec.
  - Pathways: the zigzag legs are 36.06 units with corners at x 30, 50 and 70; the curved pathway is a half circle
    (r 40) bulging to the back.
  - Round 7 circle: r 26.25, spans x 3.75 to 56.25 and z 6.75 to 59.25, so it stays on the floor.
  - Draw a path counts: a line 80 units long gets 13 counts and a half circle 125.7 units long gets 20, as the
    16-per-100 rule gives.
  - The 8 Mystery rounds match Content.
- **Done when 2:** a level tap after count 3 switched on count 4 (trace `1m 2m 3m 4h ... 8h`), and Up and down ran 40
  counts, 8 each at H M L M H.
- **Done when 3:** three trips (straight high, curved middle, zigzag low) each left the right shape, pattern and color
  (frame `paths-3ribbons.png`).
- **Done when 4:**
  - The answers are disabled during the trip.
  - Nothing gives the answer away: the level guide shows no band, the stage description names no level, the level
    buttons stay hidden until the pathway is right, and the right-pathway ribbon is a neutral gold (frame
    `mys-trip-mid.png`).
- **Done when 5:** a plain line, a smooth arc and a three-corner scribble (real drag, frame `draw-real.png`) came back
  right, both clean and with 1.2-unit jitter. A 10-unit line got tooShort.
- **Language:** plain and right for K-2 (the subtitle "Locomotor and nonlocomotor movement" is for the teacher).
- **Guardrails:** teacher led, no points or timers, 8 dots and no wrong count.
- **Rule 8:** the dance standards cover no sensitive topic here.
- **Sensitivity (rule 5):** no cultural, Native or hard-history content, so no sensitivity review is needed.

Not run by this lens: Done when 6 to 9 (stale lines, voice counts, sizes, Motion and Sound timing) belong to the Play
and Craft lenses. The real-speed hand-off from round 8 to the gallery was checked only by reading the code.
