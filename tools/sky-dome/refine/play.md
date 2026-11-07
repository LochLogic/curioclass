# Play lens: sky-dome (Curiosity No. 05), round 1

Played twice: as a grade 5 to 6 student alone at home (opened it, dragged the time dial, chased the Moon, tried the
year, went to Sydney, the equator and the North Pole) and as a teacher projecting it for grade 1 (Play at 10 min/s,
Same time each night, daylight on and off, Read). Judged against CODEX-CURIOSITY.md and VISION "Curiosities", not
lesson norms. Frames are mine in `S:/CurioClass-codex-scratch/sky-dome/play/f1` to `f5` (plus crops), and the shared
audit's frames in `S:/CurioClass-codex-scratch/sky-dome/audit-r1`.

## Short test

- **Would a kid open it unassigned?** Yes. The first drag of the time dial makes the whole sky wheel, the Moon
  and Saturn move, day floods in. That reaction comes with nothing read.
- **Would an adult play for fun?** Yes. Mars tracing its loop with Trails (f2/mars-zoom.png), Thuban at the pole in
  2800 BC, Polaris Australis over Sydney, Same time each night sliding the sky west (5 days in 6 s, clock held at
  20:33). That depth would last a month.
- **Is the real thing the interface?** Yes, but the sky is drawn stretched (first finding). The figures a student is
  told to watch turning change shape as they turn. This is the one place the short test bends.
- **Does it work with no finish line?** Yes. Lesson creep search finds no score, goal, level, sticker or finish. The
  hits ("points", "complete", "level", "correct") are code names and Manual prose.

## Findings

### 1. The dome stretches the sky, so constellations change shape as they turn
- **Where:** `src.html:1181` (`rx` set from the width, `ry` from the height, separately), and `projectVector`
  `src.html:819-826`, which scales x by `rx` and y by `ry`.
- **What:** at 1366x768 the 180 degree dome is an oval about 1240 by 470 px, so east-west angles are drawn about 2.6
  times larger than north-south ones. At 680x425 the stretch is close to 4 to 1. The Big Dipper is a long flat ladle at
  22:00 and a tall narrow one at 04:00 the same night: the same stars, a different shape. Spec "Things to do" 13 ("the
  same stars, turned") and the first reaction ("the whole sky wheels around one still point") both show this
  distortion first. The Manual admits it ("an equal-angle sky map fitted to an oval viewport"), but a student never
  reads that, and a planetarium dome has one scale in every direction. The Mars loop and Saturn's ring are drawn
  squashed the same way.
- **Seen:** `play/f1/dipper-a.png` beside `play/f1/dipper-b.png` (Denver, 2026-04-14 22:00 and 04:00, az 0, alt 45,
  FOV 90); every audit frame (`audit-r1/size-1366x768.png`, `size-680x425.png`).
- **Better:** one scale for both axes. Keep the 180 degree dome a circle and fill the spare width with the readouts
  and the dial deck, or with a wide equal-scale view when zoomed in.
- **Level:** blocker. **Tag:** family:curiosity (the real material is the interface; here it is drawn wrong).

### 2. The zoom buttons cover the W on the horizon ring
- **Where:** `.view-tools` `src.html:52` (desktop), `:179` and `:195` (narrow).
- **What:** the + and minus buttons sit on the dome's west edge, hiding the W compass letter at 1366x768, 680x425 and on
  the phone. That leaves three compass points visible on a tool built around them (stars "setting in the west").
- **Seen:** `audit-r1/size-1366x768.png` (W under the minus button), `play/crop-phonedome.png`,
  `audit-r1/size-680x425.png` (buttons over the lower-right rim).
- **Level:** should fix. **Tag:** general.

### 3. The first-run hint is spoken just after the student has already acted
- **Where:** `src.html:546-551` (the hint plays on the first pointerdown or keydown) and `act()` `src.html:540-541`
  (the same gesture hides it).
- **What:** whatever the first gesture is (Play, Zoom in, Lines, Now, even dragging the time dial itself), the voice
  says "Drag the time dial." while the line vanishes from the dome. A student who pressed Play hears an instruction
  for something else as the sky starts moving. The words no longer match the state (POLISH).
- **Seen:** audit "One held click per control" table, rows 0 to 14, 16 and 18: every control speaks "Drag the time
  dial." on its first tap. Confirmed on `play/f5/drag-dial.png`, where the hint was hidden after the drag.
- **Better:** if the first gesture is on any instrument control, say nothing; speak the hint only when the first
  gesture is a tap on the empty dome or deck, or only on Read.
- **Level:** should fix. **Tag:** family:curiosity (the browser needs a gesture before speech, so every Curiosity's
  "spoken once" hint lands late).

### 4. No constellation names anywhere, so half the "Things to do" cannot be found alone
- **Where:** no constellation label or readout exists in `src.html`. FIGURES (`:804`) are drawn as unnamed lines; the
  star card (`object-type`) gives "HR 2491 · A1Vm" but not the constellation.
- **What:** spec items 4 ("which constellation the Sun is in"), 7 (the Southern Cross), 12 (Thuban "in Draco") and 13
  (the Big Dipper) all need names a student cannot get from the dome. With Lines on, the dome shows 88 nameless stick
  figures. A grade 5 student alone at home cannot tell which one is Orion. This is also the depth a month of use would
  look for: learning the sky by name.
- **Seen:** `play/f1/noon-nodaylight.png` (the Sun with daylight off; nothing says where it is),
  `audit-r1/state-running-1366x768.png` (Lines on, no names).
- **Better:** constellation names as a lever (or tied to Lines), and a CONST row on the readout card. Real material,
  not a game.
- **Level:** should fix. **Tag:** family:curiosity.

### 5. Long star labels run over neighbouring stars and mislabel the Southern Cross
- **Where:** label placement `src.html:997-1005`, which tries right and then left of each star with no leader line.
- **What:** over Sydney (2026-05-01 20:04), "Rigil Kentaurus" starts at its star (x 498) and runs right across Crux,
  so the label sits on the Southern Cross; "Toliman" is labelled separately at the same point; Acrux and Hadar get no
  label. A student hunting for the Southern Cross (spec item 7) reads the wrong name on it. Labels are also drawn over
  other stars: a star dot sits on the P of "Pollux".
- **Seen:** `play/f3/sydney-sky.png`, `play/crop-cross.png`, `play/crop-rollux.png`; positions from `__tool.objects`
  (Rigil Kentaurus 498,389; Acrux 599,372; Mimosa 572,366; Gacrux 579,358).
- **Better:** a short tick from star to label when the label clears it, skip a label whose box covers a brighter
  labelled neighbour, and label a binary once.
- **Level:** should fix. **Tag:** general.

### 6. Typing "Sydney" says the place is not in the selection
- **Where:** `$("city").onchange` `src.html:1291-1294`.
- **What:** "Sydney" matches two bundled places (Australia, Canada), so the tool answers "Place not in bundled
  selection. Enter latitude and longitude." That is untrue: both are bundled. A student following "go to the far
  south" types the city and is told it is missing. "Paris" alone works because it is unique.
- **Seen:** `play/f3` shot "sydney": live text plus `places` filter `["Sydney · Australia","Sydney · Canada"]`.
- **Better:** "Two places match: pick one from the list" and open the list, or prefer the most populous match.
- **Level:** should fix. **Tag:** general.

### 7. The year odometer shows "-2799" for 2800 BC
- **Where:** `#year` `src.html:252-254` (astronomical year numbering, with the era beneath).
- **What:** spec item 12 says "set the year to 2800 BC". A student types -2800 and gets 2801 BC; the big window reads
  "-2799" with "2800 BC" small beneath. Two numbers for one year, and the large one is the unfamiliar one. In AD
  years the window and the line beneath say the same thing twice ("2026" and "AD 2026").
- **Seen:** `audit-r1/state-ancient-pole-1366x768.png`; `play/f1` shot "year-bc" (era "2800 BC" from -2799).
- **Better:** the window shows "2800" with a BC/AD switch beside it (a real odometer with an era flag); keep the
  astronomical year in the Manual.
- **Level:** polish. **Tag:** general.

### 8. In daylight the Sun, Moon and planets lose their names
- **Where:** `src.html:993` (`if(state.names && day<.85)` drops every label in daylight).
- **What:** dragging the time dial into the morning leaves a bright disc, a white dot and a crescent with no names
  (Venus and the Moon in `play/f5/drag-dial.png`). This is the moment a grade 1 class is asked "where is the Moon in
  the daytime?", and the dome goes quiet. Star names fading in daylight is right; Sun, Moon and planet names fading is
  a flat moment.
- **Seen:** `play/f5/drag-dial.png`, `play/f1/noon-daylight.png`.
- **Better:** keep labels for the Sun, Moon and visible planets in daylight.
- **Level:** polish. **Tag:** general.

### 9. The phone plate wraps and its rivet sits on the C
- **Where:** `.plate` `src.html:172` (`white-space:normal; max-width:250px`) with the `::before` dot at `:98-99`.
- **What:** at 375 wide the plate reads "Curio Class Curiosities · No. 05 · Sky / Dome" over two lines, and the left
  rivet dot overlaps the first letter of "Curio Class". The plate is a family mark and should read as one engraved line.
- **Seen:** `play/crop-plate.png` (from `play/f4/phone-default-tall.png`), `audit-r1/size-375x812 (iframe host).png`.
- **Better:** a smaller size or tighter letter-spacing so it fits on one line, with padding that clears the rivets.
- **Level:** polish. **Tag:** family:curiosity.

### 10. Phone: the dome is small and the hint sits on the star labels
- **Where:** phone layout `src.html:1180-1181` (`top=112`) and `#hint` `:182`.
- **What:** at 375x667 the dome is about 220 px tall (the spec asks for about 60 percent of the height), and "Drag the
  time dial." sits under N over the Capella area. Sun and Moon rise and set times are dropped on the phone, so the
  phone student loses the readouts behind spec items 3 and 5.
- **Seen:** `play/f4/phone-default-tall.png`, `play/crop-phonedome.png`.
- **Level:** polish. **Tag:** general.

### 11. Read speaks clock time as "20 hours 22 minutes"
- **Where:** `speakText` `src.html:520`.
- **What:** for a grade 1 room on a projector, "twenty hours twenty-two minutes" is not how anyone says the time.
- **Seen:** audit row 18 ("November 5, 2026. 20 hours 22 minutes. Denver.").
- **Better:** "8:22 in the evening" (or "8:22 p.m.") when at home; keep 24-hour in the readout.
- **Level:** polish. **Tag:** general.

### 12. Nits
- The time dial's focus ring overlaps its "TIME · 24 HOURS" label (`play/f1/keys-time.png`). nit, general.
- At the full 180 degree view looking straight up, the Ground lever has nothing to show, so the spec's "faint ground
  silhouette" first view does not appear (`audit-r1/size-1366x768.png`). nit, family:curiosity.

## What worked (checked, nothing to report)

- Time dial drag is direct and crosses midnight into the next date (20:35 to 08:02 next day, `play/f5/drag-dial.png`).
  Arrow and Shift-Arrow steps on the dial work and focus is visible (`play/f1/keys-time.png`).
- Motion off: Play steps 10 minutes and the sky never runs on its own (`play/f1/calm-play.png`; audit "Motion off" clean).
- Same time each night holds the clock and steps the date (5 days in 6 s). Equator, North Pole, Sydney and 2800 BC all
  give clear, distinct skies (`play/f1/equator.png`, `north-pole.png`, `play/f3/sydney-sky.png`).
- Tapping a star selects it and opens the card (Vega, `play/f5/tap-vega.png`). The Manual drawer is tidy, with
  "Things people have found" as closed details, never targets (`play/f2/manual.png`).
- Frame times at 1366x768 with 1 day/s, Lines and Trails on: median 7 ms, worst 12 ms on this PC (not a Chromebook;
  Craft owns that).

## Audit pilot

- **Leads confirmed:** none of the six leads is a fault. "Hint out of view" after every state is expected: the hint is
  meant to go after the first action.
- **Leads wrong:** the six "hint out of view" rows (see above).
- **Clean rows cited:** sizes, Motion off, resize mid-action, five clicks and two quick taps.
- **What it missed:** the stretched projection (finding 1; all its frames show it, but it cannot judge shape); the zoom
  buttons covering W (2: no clipped text, since the letter is canvas-drawn); the late hint speech (3: its table shows it,
  but it marks it "spoken", not wrong); missing constellation names (4); labels over the wrong stars (5); the
  "not in selection" message (6); the year window (7); the phone plate wrap (9).

No cultural, Native or hard-history content found. The tool leaves cultural sky stories out and credits star names as
identifiers.
