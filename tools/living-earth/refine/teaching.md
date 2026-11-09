# Teaching lens: living-earth (Curiosity No. 04), round 1

Cold lens, judged against CODEX-CURIOSITY.md, VISION.md "Curiosities: the second shape", BASELINE and the spec.
Bundle as built (1,957,170 bytes). My frames and checks: `S:/CurioClass-codex-scratch/living-earth/teaching/out/`
(numbers saved beside them as facts.json, numbers.json, nums2.json, rot.json). Shared audit:
`S:/CurioClass-codex-scratch/living-earth/audit-r1/`.

Counts: 1 blocker, 4 should fix, 4 polish, 5 nits.

## Blocker

**B1. Pin SPEED and the Arrows layer report a reference-frame drift, not how fast the plate moves.**
- Where: src.html:1660-1669 (`plateMotion`), Pin readout 1695-1696, Read text 1175, Arrows 1797-1806; spec "Things to
  do" 10 and 11.
- What: the speed and heading come from Merdith et al. 2021's 0-5 Ma rotation relative to plate 000, its absolute
  (palaeomagnetic) frame. That frame carries a large common rotation shared by every plate: North America, Africa and
  Australia all turn 2.3 to 3.0 degrees in 5 Myr about nearly the same axis, and each 10 Ma sample is exactly twice the
  5 Ma one. The readout is dominated by that drift. Against ITRF2014 plate motion poles (Altamimi et al. 2017,
  recomputed in Python):

  | Pin | Tool | ITRF2014 (GPS) |
  |---|---|---|
  | Denver, North America | 6.2 cm/yr, 253 deg | 1.6 cm/yr, 247 deg |
  | Sydney, Australia | 2.8 cm/yr, 325 deg | 5.7 cm/yr, 19 deg |
  | Perth, Australia | 4.5 cm/yr, 356 deg | 6.9 cm/yr, 34 deg |
  | London, Eurasia | 5.3 cm/yr, 0 deg | 2.4 cm/yr, 46 deg |
  | Cairo, Africa | 5.5 cm/yr, 12 deg | 2.9 cm/yr, 53 deg |
  | Lima, South America | 2.9 cm/yr, 309 deg | 1.1 cm/yr, 345 deg |
  | Honolulu, Pacific | 9.3 cm/yr, 264 deg | 7.1 cm/yr, 299 deg |

  Australia, the fastest-moving continent, reads slower than North America, and in the wrong direction. Africa reads
  5.5 cm/yr due north. A student doing "Pin your town and read how fast your plate moves" gets a number two to four
  times off any textbook or GPS figure, and the Arrows layer (frame atlantic-all.png, pin-sydney.png) shows Africa and
  most plates drifting north or west together, which hides the relative motion "two plates heading at each other" is
  meant to show. The small instrument note ("motion is the model's 0-5 Ma average, in its own reference frame") is
  true but cannot rescue a grade 6 reader; REFINE: an estimate that misleads when its assumption does not hold is a
  blocker.
- How seen: numbers.json, nums2.json and rot.json (pinData and plateMotion run in the page), ITRF2014 comparison
  computed in Python; frames pin-sydney.png, atlantic-all.png.
- Better: keep Merdith for Rewind (its job), but take present-day motion from a present-day plate motion model in a
  no-net-rotation frame (ITRF2014-PMM or MORVEL/NNR-MORVEL56; check the licence), or at least remove the common
  rotation and show motion relative to the neighbouring plate across the nearest edge (opening or closing, cm/yr),
  which is what a seismologist and MS-ESS2-3 care about. Re-check the fingernail field note against what the readout
  then shows.
- Tag: family:curiosity (a model chosen for one instrument reused for a readout it was not built for).

## Should fix

**S1. Slice draws the sea floor below the shallow earthquakes, so ridge and trench quakes look like they sit in the
water.**
- Where: src.html:974-985 (`renderSection`).
- What: quake depths are plotted at true scale below sea level, but the ETOPO profile is multiplied by 20 on the same
  axis, so a 4 to 5 km deep sea floor is drawn at 80 to 100 km. In the Mid-Atlantic section every quake (10 to 20 km)
  sits above the sea-floor line; in the Japan section the shallow cluster floats above the drawn ocean floor. The note
  "surface relief x20" is there, but the picture says the opposite of the lesson (quakes happen in rock, under the
  ridge).
- How seen: slice-mar.png, slice-japan.png, slice-peru.png (my own; the Peru-Chile and Japan sections otherwise show
  the dipping slab well, Done-when 2 Slice passes).
- Better: draw the exaggerated profile in its own strip above the 0 km line (or exaggerate only above a sea-level
  baseline), or plot quakes below the local surface. Say "sea floor" and "sea level" on the section.
- Tag: family:curiosity.

**S2. Wave and Stations disagree with their own 104 degree shadow between 99 and 104 degrees.**
- Where: src.html:735-742 (`arrival`), 1104-1106, 1096 (shadow arc), 936 (globe ring at 104 deg); Manual "Wave".
- What: the bundled iasp91 table has direct P only to 98 deg and direct S only to 99 deg. From 99 to 104 deg the
  readout says "P NO BRANCH · S NO BRANCH" while the receiver dot sits outside the drawn "S SHADOW" arc and inside the
  globe ring. From 104 to 140 deg P says SHADOW; past 140 P returns. So the instrument shows three different shadow
  edges and the words "NO BRANCH" are not explained in plain language. Also S at 98 to 99 deg arrives at 25:06 to
  25:14, past the 25:00 end of both the elapsed fader and the station trace, so it can never be reached or marked.
- How seen: nums2.json (`arrival` at 94 to 106 and 136 to 142 deg), wave-100.png.
- Better: draw the shadow from the table's real edges (about 99 deg for direct S, 98 to 140 deg for direct P), say in
  the Manual that waves bend round the core there (diffracted waves, left out), and replace "NO BRANCH" with words a
  student can read ("no direct wave arrives here"). Extend the window to 26 min or say why it stops.
- Tag: family:curiosity.

**S3. The words are written for a geophysicist, not a grade 4 to 8 student alone at home.**
- Where: Manual (src.html:550-664) and on-screen notes 459, 475, 490, 499, 507, readouts "NO BRANCH", "UNRESOLVED
  MODEL AREA", "QUAKES HELD", "FIT AMBIGUOUS".
- What: examples a grade 6 reader meets: "Finite rotations are resolved through the published plate circuit relative
  to plate 000, sampled every 5 Ma, with quaternion interpolation between samples"; "The normalized three-plane fit
  must agree with every measured circle within 200 km"; "schematic older fossil evidence · modern overlays withheld";
  "motion is the model's 0-5 Ma average, in its own reference frame"; "Tap three stations · drawn model traces · surface
  focus · iasp91". The honesty is right; the reading level is not (REFINE teaching 5, rule 4). The Manual also has no
  short plain "how to read this" line before the detail for each instrument.
- How seen: reading src.html and the frames (state-*-1366x768.png in the audit, my slice/wave/pin frames).
- Better: for each Manual section, lead with one or two plain sentences at about grade 6 ("Each dot is a real
  earthquake. Bigger dot, bigger quake. Colour shows how deep it was."), then keep the technical honesty notes under
  a "For the curious" line. Plain on-screen notes ("Rays bend through a model Earth. Arrival times from a standard
  model."). Explain S-P in one sentence where the markers are.
- Tag: general.

**S4. science-9-orbits-and-earth-s-history (HS-ESS1-5) is listed as reached, but nothing lets a student see the ages
of crustal rocks.**
- Where: spec "Map"; module codes in data/modules.csv (HS-ESS1-4; HS-ESS1-5; HS-ESS1-6).
- What: HS-ESS1-5 is about using plate motions to explain the ages of crustal rocks (sea floor older away from
  ridges). The tool has relief, quakes, a reconstruction and a model speed, but no rock or sea-floor age anywhere. The
  anchor MS-ESS2-3 is exercised by doing (fossil and mountain belts and continent shapes in Rewind, ridges and trenches
  in relief and Slice; its boundary excludes palaeomagnetic anomalies), and 4-ESS2-2 is exercised well (frames
  pacific-all.png, tonga-deep.png, hawaii.png). MS-ESS3-2 is touched only as "where quakes cluster"; the Manual
  rightly refuses forecasting, which is the code's verb, so it is thin but honest.
- Better: add a sea-floor age layer (an ocean age grid such as Seton et al. 2020, CC BY 4.0 at source, to be
  verified), readable by Pin and visible along a Slice, which also gives Hawaii's chain and the Atlantic opening real
  numbers. Otherwise drop science-9 from "Also reaches" (rule 2: never a thin activity to make a code honest).
- Tag: general.

## Polish

**P1. "Find Hawaii ... follow the chain of older islands to the northwest" (spec Things to do 12) has nothing on screen
that says older.** The chain and the Emperor bend are visible in relief (hawaii.png), but ages live only in the Manual
field note. A sea-floor or volcano age readout (see S4) would let the student find it. family:curiosity.

**P2. "Compare the visible-quake count around the Pacific rim with the rest of the world" (Things to do 13) cannot be
done.** QUAKES counts the whole sphere; the only local count is Pin's 300 km circle. The Manual itself says the 81
percent figure is not measured from the display. A hemisphere or "within the globe's view" count, or a count inside
the Edges layer's Pacific plates, would turn the field note into something the student can check. family:curiosity.

**P3. Teacher notes do not name the sensitive side.** The M8+ catalog and Strike name real deadly events (2004
Sumatra, 2011 Tohoku, 2008 Sichuan, 2015 Nepal, 2023 Kahramanmaras). Showing them as data is right (spec), but
notes.md should carry a one-line content note that some students or families may have lived through these (rule 8).
Two Support at home ideas are weak: "Ask a family member what a map leaves out" is vague and the string one needs a
paper map most homes lack; something like "find your town on the globe, pin it, and look up the last quake felt there
together" is doable tonight. Not a cultural or Native item: no sensitivity agent needed. general.

**P4. Rewind shows the answer, never the test.** The dial runs the model; the student cannot try fitting South America
to Africa themselves and then compare with the model, which is the evidence-reasoning MS-ESS2-3 asks for and what
Wegener did. A "drag a continent" fit before or beside the model would add depth without a score. Rewind itself
passes Done-when 2 (rewind-200-satl.png, rewind-200-gond.png, rewind-200-laur.png: fossil belts and the
Appalachian-Caledonian traces line up at 200 Ma; rewind-100.png shows a narrow Atlantic). family:curiosity.

## Nits

- **N1.** On load the top strip reads YEAR 1970, QUAKES 0 and the TIME fader shows 1970; moving the fader to 1970 gives
  475 quakes (the Manual says the fader includes the chosen year). Same dial position, two counts. src.html:677, 750,
  1189.
- **N2.** 525 ComCat place names contain a literal "?" for a lost diacritic ("17 km NW of Bhach?u, India", "K?h
  Sef?d, Iran"). Checked: ComCat's API returns the same, so it is faithful, but on screen it reads as broken.
- **N3.** Strike always starts with 2004 Sumatra and cycles in a fixed order; a returning student knows the answer
  before Reveal.
- **N4.** Pin plate names follow the 0.1 degree model: Reykjavik reads Eurasia (it sits on the North American side of
  the rift; "boundary area" is shown, so not a lie). Honolulu's and Mumbai's nearest volcano read "Unnamed".
- **N5.** In Rewind the depth legend (DEPTH / km) stays on screen though dots are withheld.

## Done when (teaching items)

1. Opens to the globe, no welcome; play 1970 to 2025 at the default 3 yr/s is 18.7 s. PASS (src.html:674, 1338).
2. Slice Wadati-Benioff under Japan and Peru PASS (slice-japan.png, slice-peru.png). Stations with markers on the drawn
   arrivals: offset 6 km for all 20 Strike events (numbers.json). PASS. Wave S shadow: PASS with S2. Rewind to 200 Ma
   PASS. Pin gives plate, speed, nearest volcano: works, but the speed fails B1.
3. Every number traced: 14 quakes checked against the live ComCat API by event id (Nepal 2015, Kahramanmaras 2023,
   Loma Prieta, Northridge, Bhuj, Sichuan, Tohoku, Sumatra, Bolivia 1994 deep, Kamchatka 2025, Chimbote 1970, Okhotsk
   2013, Fiji 2018, Tangshan): date, magnitude, position (0.01 deg) and depth all match. Total 26,230 matches ComCat's
   count for M5.5+, eventtype=earthquake, 1970 to 2025 exactly; per-year counts for 1970, 1990, 2011 and 2025 match
   (475, 522, 714, 514); 44 M8+ events match ComCat's 44. iasp91 times (P 30 deg 6:10, P 90 deg 13:01, S 90 deg
   23:56), PREM core radii (3480 and 1221.5 km) and the S-P to distance inversion (100 s to 967 km) are right. Plate
   speeds FAIL (B1). Field notes (M9.5 Chile 22 May 1960, 81 percent Pacific rim, Lehmann 1936, about 2.5 cm/yr
   Atlantic, Tonga near 700 km: bundled deepest is 700 km, Fiji 1985) agree with their cited USGS pages.
4. Sources and licences are in the Manual and tool.draft.json. PASS (licences not re-verified by me beyond the
   records cited).
10. No score, goal, level, sticker or finish; the Stations offset is a distance. PASS (lesson creep grep clean).

Giveaways: Strike hides the event until Reveal (src.html:1068); Circles use the student's own markers. Fine apart from
N3.

## Audit pilot

- Leads confirmed: none of the 523 is a teaching problem. The "keep region" and "text hidden" leads on #marker-p-out
  and #marker-s-out at 680x425, 800x500 and 375x812 are real in the sense that the values sit over the range inputs
  (state-stations-680x425.png), but they stay readable there.
- Leads wrong (grouped by cause): 460 "overlap" rows are the full-bleed #globe canvas under its own overlays (legend,
  hint, position, toolbelt, event list): by design. The 7 "hint out of view" rows are wrong: the hint is plainly on
  screen at 1366x768 (size-1366x768.png). The 45 "text hidden" rows in the manual state are the modal Manual dialog
  covering the station, as it should. The 4 "keep region" rows for #play, #manual, .maker and .power are the same
  modal.
- What it missed (it cannot judge these): B1 plate speeds two to four times off and in the wrong direction; S1 sea
  floor drawn below the quakes; S2 the three different shadow edges and the unreachable S arrival at 98 to 99 deg;
  S3 reading level; S4 the unexercised HS-ESS1-5; N1 the 0 versus 475 count at the same dial position; N2 the "?"
  place names.
