# Play lens: living-pond (Curiosity No. 13), round 1

Cold Play lens, 2026-11-06. Played twice: as a grade 5 student alone at home, and as a teacher projecting it.
Bundle `tools/living-pond/living-pond.html` as built. My frames: `S:/CurioClass-codex-scratch/living-pond/play/shots/`
(scenario JS in `play/mk.py`, `play/mk2.py`). Shared audit: `S:/CurioClass-codex-scratch/living-pond/audit-r1/`.

## Short test (Curiosity)

- Would a kid open it unassigned? Yes. It opens alive: heron in the shallows, minnows schooling, a turtle in the mud,
  a chart pen moving. One tap on Minnow drops one in and the count ticks (`tap-minnow.png`). Netting all the minnows
  and watching the snails crash and the heron leave is a real "whoa" (`net-all-minnows.png`).
- Would an adult play for fun? Yes. Ten winters at Fast draw a real predator-prey cycle on the chart (`year10-whole.png`);
  overfeeding gives a true winterkill in year 2 with the minnows crowding the surface (`feeder-lots.png`).
- Is the real thing the interface? Mostly. The tank and the chart are the interface. The bottom third is a row of
  web-form dropdowns (finding 5), and the winter drama is mostly invisible (finding 1).
- Does it work with no finish line? Yes. No score, goal, level, sticker, toast or finish screen found.

The short test passes. No blockers. The findings are about the drama reaching the student and the instrument feel.

## Findings

1. **should fix** · family:curiosity · src.html:375 (`logEvent`), 622 (`L` holds only the hint), 1617 (dial)
   The pond's best moments happen silently. Ice, ice-out, "Heron flew off", "Turtle walked off", "Snails gone" and
   "Winterkill conditions" are written only to the pond log, which lives inside the Manual drawer. Nothing on the
   instrument says them: there is no log strip on the tank (spec Look: "log right"), none of the spec's event lines
   ("Ice. No new air gets in until spring.", "Oxygen's low. The minnows are gasping at the top.", winterkill, heron or
   turtle left, "The snails are gone.") is in `L` or voice/lines.json, and the oxygen dial has no 3 and 2 marks on its
   face, only "3 gasp / 2 kill" as corner text. In `feeder-lots.png` (year 2 week 50, 0.6 mg/L, winterkill logged) the
   only cues are a needle near 0 and fish at the top; a student who looked away misses what the spec calls the pond's
   best lesson. Better: a one-line latest-event readout on the tank rim, the spec's event lines (once per 20 s), and a
   red band from 0 to 3 on the dial face.

2. **should fix** · general · src.html:142 (`@media(max-width:900px) #hint{display:none}`)
   The only first-run instruction is hidden at every width under 900 px: 680x425, 760x900 (tablet portrait) and
   375x812. Voice speaks the hint only after the first touch (src.html:662), so a student on a tablet or a narrow
   Chromebook window gets no instruction at all before acting. Seen in `narrow-680-winter.png` and audit
   `size-680x425.png`, `size-760x900.png`, `size-375x812 (iframe host).png`. Better: keep the one-line hint on the
   tank rim at every size.

3. **should fix** · general · src.html:42, 86-87 (`#whole` pressed style)
   "Whole run" turns white on the cream chart paper when pressed: the toggle vanishes exactly when it is on, so a
   student cannot see it to turn it off. Seen in `year10-whole.png`, `feeder-lots.png`, `net-all-minnows.png`
   (zoom: `play/z-whole.png`).

4. **should fix** · general · src.html:531-535 (yearly reset), `sync()` Energy ledger
   Spec thing-to-do 4 is "leave the Energy lens on for a whole year". At week 51 the ledger reads caught 25,114 and
   heat out 25,674 (102 percent); one week later, the moment the year is done, every line drops to 0 and "0.0% OF SUN"
   (`energy-yr1.png`, year 2 week 00). `s.lastEnergy` is kept but never shown. Better: show last year's totals beside
   this year's, or hold last year's ledger until the new year has a few weeks of data.

5. **should fix** · family:curiosity · src.html:228-244
   Seven of the instrument's controls (speed, lens, feeder, bottom, decomposers, canopy, year) are native `<select>`
   dropdowns styled as form fields. On every frame the bottom third reads as a settings page, not a study tank, and
   each change is two clicks into an OS menu. The tray and Run feel like an instrument; these do not. Better: detented
   dials or toggle switches with the value printed on them (Craft owns the look rule; flagged here for feel).

6. **should fix** · family:curiosity · src.html:1092-1108 (`follow`, `updateTracker`); Enter on the tank in Matter
   Following a dot rarely tells the promised story (muck, water and air, algae, minnow, muck again). I followed one dot
   from each of 8 starting pools for 52 weeks: only dots that started in an animal ever touched an animal; water and
   air, floating algae, stem algae, muck and decomposers never reached one (for example "Water & air > Floating algae >
   Muck > Decomposers > Muck"). Enter in Matter always follows Muck, which stayed "Muck" for 26 weeks
   (`matter-follow.png`): a long flat wait for a keyboard student. Better: Enter picks the dot nearest the drop point,
   and the trip box says how long the dot has been where it is.

7. **should fix** · general · src.html:716
   Words do not match the state: "The pond is full of minnow.", "...of heron.", "...of turtle.", "...of snail."
   (checked by adding to each cap). Use plurals, or "No room for more minnows."

8. **should fix** · general · Manual drawer (src.html, `#manualbody`)
   A solo grade 5 student is sent to the Manual for every explanation, and it reads as a model specification:
   "counterfactual", "flow-weighted probabilities", "outgoing flows share a proportional limit", "Caught is gross algae
   growth x 10". The "Who eats whom" table is clear; most of the rest is not readable at the anchor grade. Better: a
   plain first paragraph per section at grade 5, with the model detail below it for adults.

9. **polish** · general · src.html:611, 1538 (chart dashes)
   The actual lines for snails, minnows and nymphs are already dashed, and ghosts are dashed [5,4] at 0.85 alpha, so the
   "dashed ghost of the untouched pond" is hard to tell from the real snail trace (`tap-minnow.png`,
   `net-all-minnows.png`). Better: ghosts far paler (about 0.35) or thin dotted grey.

10. **polish** · general · src.html:784
    Tray labels read "36 · 1 = 1", "71 · 1 = 2". A student cannot tell this means "36 here, one drawing stands for 2".
    In net mode it wraps to "1 =" over "1" (`net-swipe.png`). Better: "36 here", and the multiplier only when above 1.

11. **polish** · general · src.html:1157-1159
    Three turtles asleep in the mud are drawn 35 px apart with a 77 px sprite, so they pile on one another
    (`limits-fps.png`). Spread them, or put the extras on the log.

12. **polish** · general · src.html:1363
    On an Empty pond the tank reads "TURTLE WALKED OFF · HERON FLEW OFF" though neither was ever there
    (`empty-pond.png`). Better: "NO TURTLE · NO HERON".

13. **polish** · general · drawTank, ice
    Winter is the drama the spec promises ("ice creeps in from the edges with a crackle"), but under ice the water stays
    the same bright teal with a thin pale band at the top, and the fish swim as in spring (`ice-winter.png`). The
    backdrop carries the season, not the water. Better: a thicker ice sheet, a darker dimmer water column, slower fish.

14. **polish** · general (teacher projecting) · chart legend, end labels, meter text
    From the back of a room the chart's line keys and end labels ("A 36", 10 to 12 px monospace) and the dial's
    "3 gasp / 2 kill" (10 px) cannot be read. The tank projects well; the chart, which carries the story, does not.
    Better: larger end labels at 1280 px and up.

15. **nit** · general · `.station` title
    "Living Pond / FIELD STATION / 13" sits over the log and cattails at top right, so "FIELD STATION / 13" is half lost
    in the art (`size-1366x768.png`, `tap-minnow.png`).

Checked and fine: a tap on Minnow drops one the same frame; ice arrives at week 41 (about 20 s at Normal); the heron
flies off in winter and returns in spring; food arrows on inspect are clear and labelled, absent kinds dashed
(`inspect-key.png`); New offers Save first (`new-confirm.png`); 60 fps at every add limit at Fast (headless,
`limits-fps`); the matter total stays 742.0 over ten winters; calm mode keeps time (the tick ignores Motion; audit
"Motion off" clean).

Counts: blocker 0, should fix 8, polish 6, nit 1.

## Audit pilot

- Leads confirmed: "hint out of view" at 680x425, 800x500, 760x900 and 375x812 (finding 2; a CSS rule, not a scroll).
  The 375x812 tray scrolls sideways with Decomposers, Food and Net out of view; the spec asks for a scrolling tray row
  there, so not reported.
- Leads wrong (noise): every `#pond` overlap row (the canvas fills the tank and controls sit on it by design);
  "text under 10 px 0.0px" on the TIME and LENS labels at 375 (deliberately font-size 0; the selects keep aria-labels);
  "keep region #ledger covered" (the ledger is an overlay on the canvas); "#run/#speed/#tray hidden" in manual and saved
  (the modal drawer makes main inert); "hint out of view" at 1000 px and up in states (the state's first touch had
  cleared it); "welcome not heard after first tap" (BASELINE rule 16).
- Missed by the audit: the invisible pressed "Whole run" toggle, the Energy ledger zeroing at year end, the status
  grammar, stacked turtles, the Empty pond's "walked off / flew off" label, the silent winterkill and missing event
  lines, the Matter trip that rarely reaches an animal, and the Manual's reading level.
