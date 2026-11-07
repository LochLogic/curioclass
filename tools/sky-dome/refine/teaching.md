# Refine, Teaching lens: sky-dome (Curiosity No. 05)

Judged against CODEX-CURIOSITY.md and VISION "Curiosities: the second shape", not lesson norms. Bundle as built
(`tools/sky-dome/sky-dome.html`), driven in headless Chrome (zone America/Denver). My frames and numbers are in
`S:/CurioClass-codex-scratch/sky-dome/teaching/` (`out/*.png`, `calc-out.json`, `calc2-out.json`). Reference values
fetched today from JPL Horizons (apparent RA/Dec, geocentric) and the USNO API (Denver rise/set, 2026 lunar phases).

Short version: the astronomy is excellent. Every position, time and phase I checked is right, well inside the spec's
tolerances. The gaps are in what a student can *find out* with it: no constellation is ever named, the Sun has no
distance, one reach module is not taught at all, and the Manual skips seasons.

## Findings

1. **No constellation is named anywhere.** `src.html:953` draws `figure.slice(1)` only. Every figure's name
   (`DATA.figures[i][0]`, for example "Andromeda") is bundled but never shown, either on the dome or as a row on the
   object card. Several of the spec's Things to do cannot be answered: #4 "find which constellation the Sun is in",
   #7 "find the Southern Cross" (Acrux and Mimosa are labelled, but nothing says Crux) and #13 "find the Big Dipper"
   (Dubhe and Alioth are labelled, but there is no Ursa Major). Star patterns are the heart of the anchor's 1-ESS1-1.
   Better: a CONST row on the star, Sun, Moon and planet card, plus faint figure names while Lines is on.
   Seen: `out/noon-daylight-off-lines.png` (June 21 noon, Daylight off, Lines on, Sun selected: the Sun sits among
   lines between Taurus and Gemini, with no name anywhere), and the audit's `state-southern-sky-1366x768.png`.
   **should fix**, family:curiosity.

2. **The science-9 reach (HS-ESS1-1, HS-ESS1-2, HS-ESS1-3) is not taught by anything in the tool.** Those codes
   cover the Sun's life span and fusion, Big Bang evidence and stellar nucleosynthesis. Sky Dome shows positions,
   magnitude, B−V and an estimated temperature. That touches stellar properties, but none of the three codes.
   No activity in this instrument would reasonably teach them, so drop science-9-stars-and-the-big-bang from "Also
   reaches" (`spec.md:12-13`, and wherever the map row is written). Seen: code read of every readout
   (`updateObject`, `src.html:1103-1138`) against `data/modules.csv`. **should fix**, general.

3. **The Sun has no distance, so the 5-ESS1-1 reach can't be read off the instrument.** That module is "the Sun's
   apparent brightness compared with other stars depends on distance". The Sun card shows MAG −26.74 but no DIST
   (`src.html:1120-1128`). Planets get au and the Moon gets km. The comparison the standard wants (Sun 1 au, about
   8.3 light minutes, against Sirius at 8.6 ly) is therefore impossible. Add DIST to the Sun (au, plus light
   minutes). Also, of the 14 verified distances, the only bright-but-far star is Betelgeuse. Rigel, Deneb, Canopus
   and Antares all say "not verified", but they are the classic contrast with Sirius for Thing to do #11 ("some are
   bright because they are close"). NASA fact pages exist for at least Rigel and Canopus. Seen: `calc2-out.json`
   `sunCard` and `rigel`. **should fix** (the Sun DIST row); the extra star distances are polish. general.

4. **The Manual leaves out seasons and the Sun's path**, which the spec lists in its contents (`spec.md:72-73`) and
   which the anchor's 1-ESS1-2 (daylight across seasons) and MS-ESS1-1 depend on. "Why it changes"
   (`src.html:336-341`) explains the daily spin, why the night stars change through the year, Moon phases and planet
   loops. It never says that Earth's tilt makes the Sun's path higher and longer in summer, which is what the DAYLIGHT
   readout shows. Add a short paragraph, and add a daylight entry to "Things people have found". The instrument
   gives real numbers that match USNO: Denver 14 h 59 min on June 21 and 9 h 21 min on December 21. Seen: Manual
   read in full, plus `state-manual-1366x768.png`. **should fix**, family:curiosity.

5. **Read speaks clock time as a duration: "20 hours 22 minutes".** `speakText`, `src.html:520`, confirmed in
   audit row 18 ("November 5, 2026. 20 hours 22 minutes. Denver. ..."). The grade 1 class hearing this on a
   projector will take it as an amount of time, not a time of day. Better: "8:22 in the evening" (or "twenty
   twenty-two" for the 24-hour readout). BC years are spoken "2800 B C", which is fine. **should fix**, general.

6. **The Manual's language sits above the grade band and is mostly provenance.** Grades 5 to 9 drive this alone.
   Examples: "precessed to the chosen date" (309), "proleptic Gregorian calendar" (306), "truncated periodic
   expansion" (354), "equal-angle sky map fitted to an oval viewport" (356), "local mean solar time (longitude divided
   by 15)" (298). The honesty section and the sources section (352-442) read like a build log: 893 vertices matched,
   the Maradi/Niamey correction, "Factual numbers, not a copied protected presentation". All of it is honest, but a
   student looking for "why does the Moon rise later" wades through it. Better: plain sentences first, with each
   technical term glossed once. Move the dataset audit trail into a collapsed "Sources and checks" `details`, where
   the BSD terms already sit. **polish**, family:curiosity.

7. **Sirius's distance is shown two ways.** The card says "DIST 9 ly ≈" (`src.html:1123` rounds to whole light
   years). The Manual's found-note (349) and the spec say "about 8.6 light years". Alpha Centauri also becomes "4 ly"
   from 4.3. Anything shown twice should match: show one decimal under about 20 ly. Seen: `calc2-out.json` `card`.
   **polish**, general.

8. **"DIST not verified" reads as doubt about the star**, not as "not in this set" (`src.html:1123`). A student
   tapping Rigel may think its distance is disputed. Better: "not in this set" or "no checked value". **nit**,
   general.

9. **Compass letters at the poles.** At the South Pole frame the ring shows N, E, S and W as usual, but from
   either pole every direction is north (or south). The letters there come from an arbitrary meridian. Thing to do #6
   sends students to the poles, so either a one-line Manual note or dropping the letters when |LAT| > 89.9 would keep
   the ring from teaching something false. Seen: `state-southern-sky-1366x768.png`. **nit**, general.

10. **Year entry uses astronomical numbering.** Thing to do #12 says "set the year to 2800 BC", but typing −2800
   gives 2801 BC (the Manual says to enter −2799). The era label under the odometer does show "2801 BC", so nothing
   lies, but a kid will miss it. It could accept "2800 BC" typed, or the Up/Down steps could make the BC side
   obvious. **nit**, general.

## Standards on the module

- **1-ESS1-1 (anchor, patterns of Sun, Moon and stars):** taught. Running time shows rising and setting and the
  still pole. The date wheel and Same time each night show the seasonal drift. Stepping days shows phases, LIT and
  AGE. Weakened only by finding 1.
- **1-ESS1-2 (anchor, daylight across the year):** taught by the DAYLIGHT readout, which matches USNO. Missing its
  Manual explanation (finding 4).
- **5-ESS1-2 (reach, shadows, day and night, seasonal stars):** day and night and seasonal stars are taught. Shadow
  length and direction are not: nothing shows a shadow. A small SHADOW readout on the Sun card (a 1 m stick's shadow
  length and direction from Sun ALT and AZ) would cover it; otherwise say the reach is partial. **polish**.
- **5-ESS1-1 (reach):** finding 3.
- **MS-ESS1-1 (reach, phases, eclipses, seasons):** phases are strong. Seasons are there in the readouts but not
  explained (finding 4). Eclipses can't be watched in the shadow sense ("No eclipse shadows are modelled"), though
  Sun and Moon conjunctions are visible. Acceptable as a reach.
- **HS-ESS1-1, -2, -3 (reach):** finding 2.

## Done when (spec)

| # | Item | Result | Evidence |
|---|---|---|---|
| 1 | Opens on tonight over the time-zone city, no welcome, no permission | PASS | audit `size-1366x768.png`; zone America/Denver gives Denver 39.74, −104.99 |
| 2 | Ten stars within 0.1°, five planets within 1° | PASS | 12 Yale stars against SIMBAD J2000, all within 0.0002°. Horizons apparent RA/Dec: 7 bodies on 2026-11-05 plus Sun, Moon, Venus, Mars and Jupiter on 2026-03-20 and 2027-02-19 (17 checks), worst Saturn 0.074° |
| 3 | Denver solstices within 2 min of USNO | PASS | June 21: 05:32 / 20:31 (USNO 05:32 / 20:31). Dec 21: 07:17 / 16:38 (USNO 07:17 / 16:39) |
| 4 | Moon phase and age match USNO for three dates | PASS | Computed new Moons 2026-10-10 15:51 and 11-09 07:03 (USNO 15:50 and 07:02). At USNO first quarter LIT 50.0%, at full 99.8%, at last quarter 50.0%. Same time each night steps `addDays` at a fixed clock time (code read, not filmed) |
| 5 | 2800 BC puts Thuban within about 2° of the pole | PASS | rim reads "THUBAN · POLE OFFSET 0.1°" |
| 6 | Keyboard and 60 px targets | not mine | audit held-click and Enter-twice rows clean; Craft owns it |
| 7 | 60 fps | not mine | Craft |
| 8 | Layout and plate lower-left | cited | audit sizes clean |
| 9 | Motion off | cited | audit "Motion off: clean" |
| 10 | No network; sources in Manual and draft | sources PASS | network is Craft's |
| 12 | No score, goal, level, sticker or finish | PASS | lesson-creep grep of src.html: no hits; voice has one line, the hint |

## Facts spot-checked (second source mine)

All matched: 12 star positions (SIMBAD J2000); 17 Sun, Moon and planet positions (JPL Horizons); Denver solstice
rise and set (USNO); 2026 new Moon times (USNO); Thuban 0.1° from the pole at 2800 BC (NASA SVS 13512 says about
2800 BC); Venus greatest elongation over 2026 to 2030 computed at 47.01° (NASA: about 47°); Mars 2027 retrograde
computed 2027-01-13 to 04-03 (published: about Jan 12 to Apr 2); Polaris altitude 40.19° at latitude 39.74°;
sidereal drift 3.94 min a day; Sirius −1.46, Betelgeuse B−V +1.85, Rigel −0.03 (BSC5); distances Sirius 8.6,
Procyon 11.4, Altair 17, Vega 25, Arcturus 37, Capella 43, Alpha Centauri 4.3, Betelgeuse 650 (NASA pages; Betelgeuse
is uncertain, about 550 to 700, and the card marks it ≈); daylight at the equator on Dec 21, 12 h 08 m; Sydney on
June 21, 9 h 53 m. No readout lies, and the dataset is not oversold: the 14 distances, 333 names and 1,238 places
are stated as selections.

## Notes, home ideas, guardrails

`notes.md` is true of this tool. The home ideas are ones a family can do tonight, with a Sun-safety line. Grade 1 is
teacher-led per the spec and the notes. No hard history, health or Native content. Cultural sky stories are omitted
and star names are given as IAU identifiers with no origin claims, so **nothing to send for a sensitivity review**.
If sky stories are added later (spec Open questions), they need one.

## Audit pilot

- **Leads confirmed:** none.
- **Leads wrong:** all six ("hint out of view: Drag the time dial." in running, star-readout, southern-sky,
  ancient-pole, phone-place and deep-readout). Each state starts with an action, and a Curiosity's hint is meant to
  go after the first action. Correct behaviour, not a fault.
- **What it missed:** no constellation names (it can't judge whether a task is answerable); Read speaking the time
  as a duration (it logged the line but can't judge wording); the Sun card missing DIST; Sirius 9 ly on the card
  against 8.6 in the Manual; compass letters at the poles; the Manual missing seasons.
