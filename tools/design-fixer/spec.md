# Design Fixer

## One idea
Squint at a broken poster to see where the eye lands first and which way it tips, then move, resize and recolor until the eye lands where the poster needs it; a before-and-after wipe shows how far you came.

## Not like
- brand-builder (9-12, builder): designs a logo and brand kit from scratch. Here nothing is designed from scratch: each poster arrives broken and the job is diagnosis and repair against live meters.
- frame-it (6-8, lab): moves a camera over a photo scene (rule of thirds, leading lines). Here the camera never moves; you move the parts of a flat layout.
- vanishing-point-studio (6-8, studio): perspective drawing. No depth here at all.
- storyboard-studio (9-12): shots over time. Here one still poster.
- art-through-time (6-8, same group): history; no real artworks here, every poster is drawn in code.
- near-and-far (3-5, same group): also a puzzle of moving parts, but its meter is depth; here the meters are balance, contrast, emphasis, rhythm and unity.

## Who and how
- Grade 6-8, visual arts, module "Principles of Design (Visual Arts)".
- Topic line: principles of design: balance, contrast and emphasis
- Driver: students (laptops, alone or in pairs); a teacher can project the Squint view for a class "where did your eye go first?" 15 to 30 minutes.
- Standards: NCAS VA:Cr1 (generate and conceptualize ideas), VA:Cr2 (organize and develop), VA:Re8 (interpret intent and meaning).

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound`. Modes (`.seg`): `Studio` (explore, the default), `Fix` (ten puzzles).

Layout in both modes: the stage is a cutting mat (dark green-gray with a faint grid) holding one portrait poster (ratio 1 : 1.414). Under the poster, the `Squint` slider. The panel holds the meters, then the editing tools.

**Studio.** Opens on the "Bake Sale" poster (Content), broken, with every meter live and no goals. A `Poster` menu loads any of the ten posters in their broken state. Everything is editable. `Reset poster` restores the broken start.

**Fix.** A list of ten posters (two per principle, then a final mix). The panel top shows the client's note (one or two sentences), the goals with ticks, and `Hint`. Goals tick live. When all goals are met: the poster gets a "Fixed" stamp (icon and word), the `Before and after` button appears, and `Next poster`. Posters are never locked; `Previous` and `Next poster` always work. `Start over` restores this poster. Solved posters are remembered on this device (localStorage `design-fixer-solved`), cleared by `Clear progress`.

**Squint slider** (both modes): from 0 (sharp) to 10 (blurred up to 12 px and 70% grayer). At 3 and above, numbered eye-path badges 1, 2, 3 appear on the three elements with the highest pull (Content "Meters"). A `Squint` button jumps to 7 and back.

**Meters** (panel, always visible, each with a small drawing, a word state and the number):
- Balance: a seesaw under the poster's center line that tips toward the heavier side; reads "Balanced" when the tilt is within 8%, else "Tips left 23%".
- Contrast: the lowest text contrast ratio on the poster and which text it is ("Date: 1.9:1, too faint. Needs 4.5:1."), or "All text readable".
- Emphasis: "Eye lands first on: Title". When the first and second are close (first less than 1.3 times the second): "No clear winner: Title and Photo tie."
- Rhythm: for posters with a repeated set: "Gaps: even" or "Gaps: uneven (from 12 to 40 px)".
- Unity: fonts used, colors used (not counting black, white and the background), and left edges ("3 fonts, 5 colors, 4 left edges").
A footnote under the meters: "These meters are a model of how eyes tend to move, not laws."

**Editing tools** (panel, for the selected element): `Bigger`, `Smaller`, color swatches (the poster's palette of eight plus black and white), `Bold`, `Font` (Sans, Serif, Display), `Bring forward`, `Send back`, and `Lock` shows when an element is locked by the brief. On the poster: drag to move; a corner handle resizes; alignment guides (thin cyan lines) appear when an edge or center lines up with another element or the poster's center within 4 px, and the element snaps there.

**Before and after.** Over the poster, a vertical wipe line with a handle: left of it the broken start, right of it the student's fix. Drag the handle or use arrow keys. `Close` returns to editing.

## Content
Every poster is a list of elements: `{id, kind: text|shape|icon, text, x, y, w, h, color, font, bold, locked}` in poster units (0 to 1000 wide, 0 to 1414 tall). Events are made up; no real brands, schools or people.

1. Bake Sale (balance). Note: "Everything is crammed on the left. It looks like it's falling over." Broken: title, cupcake icon, date, place and price all left of center. Goals: Balanced.
2. Lost Cat: Biscuit (balance, asymmetry). Note: "Keep the big cat picture on the left. Make the poster still feel steady." Broken: a large dark cat silhouette (locked, left), small light text on the left too. Goals: Balanced with the cat still left (locked).
3. Science Night (contrast). Note: "Nobody can read the date or the time." Broken: pale yellow text on white. Goals: All text readable.
4. Jazz Band Concert (contrast). Note: "The whole thing is dark and the title disappears." Broken: navy title on a black background, title not bold. Goals: All text readable; title is bold.
5. Robotics Tryouts (emphasis). Note: "People keep missing the date." Broken: date small and pale, a big gear icon dominates. Goals: Eye lands first on the date, clear winner.
6. Garden Club (emphasis). Note: "Everything is shouting. What is this poster even for?" Broken: title, three flower icons, time and room all the same size and color. Goals: Eye lands first on the title, clear winner; all text readable.
7. Recycling Drive (rhythm). Note: "The four bins look like they were thrown on." Broken: four bin icons of different sizes, uneven gaps. Goals: Gaps even (spread within 10% of the mean gap); the four the same size (within 5%).
8. Talent Show (rhythm). Note: "The schedule is hard to follow." Broken: five schedule lines with uneven line gaps and three star icons at random spots. Goals: line gaps even; the three stars in a row with even gaps.
9. Library Book Swap (unity). Note: "It looks like five different posters glued together." Broken: five fonts' worth of variety (only three fonts exist, so it uses all three plus bold mixes), six colors, ragged left edges. Goals: 2 fonts or fewer; 3 colors or fewer; 2 left edges or fewer.
10. Car Wash (all). Note: "Make it work: steady, readable, and the price is the first thing people see." Goals: Balanced; All text readable; Eye lands first on the price; 2 fonts or fewer.
Hints, one per goal, for example: Balance "Drag something heavy toward the light side, or make the light side bigger." Contrast "Tap the faint text and try a darker color." Emphasis "The eye goes to the biggest, darkest, brightest thing. Make the date win." Rhythm "Turn on guides and line the gaps up." Unity "Use the same font for everything except the title."

**Meters** (the model the tool computes; numbers shown in the panel):
- Contrast per text: WCAG 2.1 contrast ratio between the text color and the color behind it. Readable: 4.5:1 or more; large text (cap height at least 3% of poster height, or bold at 2.4%) needs 3:1.
- Pull of an element: sqrt(area) times (|L* of element minus L* of background| / 100 + chroma / 150), where L* and chroma are CIELAB. Eye path = elements in order of pull.
- Visual weight: area times the same contrast term. Tilt = (weighted mean x minus poster center x) / (poster width / 2). Balanced: |tilt| 0.08 or less.
- Rhythm: the gaps between neighbors in a repeated set; even when (max gap minus min gap) is 10% of the mean or less.
- Unity: count distinct fonts (font plus bold counts as the same font), distinct colors (by hex, not counting #000, #fff, the background), distinct left edges among text blocks (edges within 4 units count as one).

## Interactions in detail
- Selection: tap an element; Tab cycles elements in reading order after the panel controls; arrows nudge 2 units (Shift 20); `+` and `-` resize 5%; Escape deselects.
- Meters update on every move (throttled to animation frames). Moving a goal from met to unmet un-ticks it silently; the Fixed stamp stays once earned for that poster.
- Elements cannot leave the poster (clamped). Minimum text size: cap height 1.2% of poster height; maximum: 20%. Locked elements show a lock icon and cannot move or change color; they can still be selected to read their numbers.
- Squint blur is a CSS filter on a copy of the poster, so editing still works while squinting; the badges sit on top, unblurred.
- Ties in pull: within 2%, both are badged the same number and Emphasis says "tie".
- Before and after uses the stored broken start; with Motion off the wipe follows the handle with no easing.
- Studio edits are not saved (Studio is play); Fix progress is.
- Sizes: the poster fits the stage height (90%) at real pixels; text inside it is poster content and scales with the poster, so at the 680x425 preview the panel shows the meters in a compact two-column grid and the poster's smallest text may drop below 10 px (allowed: the meters still read in full). At 375 wide the poster sits on top, the Squint slider under it, then meters, then tools.

## Look
- Accent (`--brand`) #4338ca electric indigo. Paper (panel) #f5f5f2, ink #1d1d22, muted #5c5c66; cutting mat #33403b with grid lines at 8% white; alignment guides #22d3ee; Fixed stamp #c2410c with a check icon.
- Contrast: white on brand 7.9:1; brand on paper 7.2:1; ink on paper 15.4:1; paper on mat 9.9:1; muted on paper 6.1:1.
- Each poster has its own palette (chosen so the broken state really fails and a fix exists inside the palette; the builder checks every goal is reachable with the palette in Python).
- Different from frame-it (dark orange), vanishing-point-studio (charcoal and red), art-through-time (parchment and oxblood).

## Art
None: posters, icons (cupcake, cat silhouette, gear, flowers, bins, stars, car, book) and the mat are drawn in code as SVG.

## Voice
Bank voice: `big-sister` (an older student who has made a lot of posters; different from every tool in this group and from frame-it and vanishing-point-studio, which have no voice). Style: friendly, quick, a little wry.
- welcomeStudio (how): "Drag the Squint slider to see where your eye lands first. Then tap anything on the poster to change it."
- squintHow (how, first time Squint reaches 3): "The numbers show where the eye goes first, second and third."
- welcomeFix (how): "Read the client's note. Fix the poster until every goal has a tick."
- each poster's note (how, once when the poster opens): the notes in Content.
- goalMet (event, per goal, stale if the goal un-ticks before it plays): "Balance: done." / "Contrast: done." / "Emphasis: done." / "Rhythm: done." / "Unity: done."
- fixed (event): "Fixed. Tap Before and after to see the difference."
- beforeHow (how): "Drag the line to wipe between the broken poster and your fix."
- lockedTap (event, stale on the next tap): "That one is locked. The client wants it there."
- Hints are spoken when `Hint` is pressed (event).

## Family engine
None.

## Sources
- NCAS Visual Arts VA:Cr1, VA:Cr2, VA:Re8: https://www.nationalartsstandards.org/
- Contrast ratio formula and the 4.5:1 and 3:1 thresholds: W3C, Web Content Accessibility Guidelines 2.1, Success Criterion 1.4.3, https://www.w3.org/TR/WCAG21/#contrast-minimum
- Visual weight grows with size, darkness against the ground and color strength; balance around a center: Rudolf Arnheim, Art and Visual Perception (University of California Press, 1954, rev. 1974), chapter 1 "Balance".
- Contrast, repetition, alignment and proximity as layout principles: Robin Williams, The Non-Designer's Design Book, 4th ed. (Peachpit, 2014).
- CIELAB L* and chroma: CIE 15:2004 Colorimetry (the conversion is standard; the builder uses the D65 sRGB formulas).
- The Pull and weight formulas are this tool's own model, labeled on screen as a model.

## Done when
1. Every poster's broken start fails its goals and has a reachable fix inside its palette (Python check of the meters on a reference fix for each).
2. Squint at 7 shows badges 1 to 3 matching the computed pull order; editing works while squinting.
3. Balance: moving the cupcake across the center flips the seesaw; the tilt number matches a recomputation by hand for one layout.
4. Contrast meter numbers match WCAG ratios computed in Python for three color pairs.
5. Before and after wipes between the stored start and the fix; keyboard moves the wipe.
6. Locked elements cannot move and say so.
7. Meters and the selected element's tools are visible without scrolling at 1366x768 and 1280x720; the poster and Squint slider are on screen at every STANDARDS.md size.
8. How lines once in five edits in a row; goalMet lines every time a goal ticks.
9. `Clear progress` empties localStorage.
