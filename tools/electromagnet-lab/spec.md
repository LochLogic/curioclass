# Electromagnet Lab

## One idea
Four lab groups' magnets lifted 6, 24, 0 and 5 paper clips: the student compares their rows, turns each difference
into a question, and answers it on the bench with fair, repeated tests, finding that the pull grows in step with turns
and current, needs a steel core and fades fast with distance; then a compass shows the invisible field doing the
pulling across empty space.

## Not like
- magnet-maze (gr 3 puzzle, concept): steers a ball with permanent magnets and solves balloon levels by eye. Here the
  magnet is a coil you wind and power, every result is a count from three trials in a table, and the questions are
  about how much (twice the turns, twice the clips). Its balloon is a level to beat; here the balloon is a measured
  test of rubbing and gap with a curve that levels off.
- circuit-builder (gr 11 sandbox, spec): spins a coil to make current and feels the load push back. Here current makes
  a pull; no generator, no circuit building, no watts.
- field-lines (gr 11 sandbox, built): twin gravity and electric field maps from placed masses and charges, 1/r squared.
  Here one real coil on paper, a compass you drag and filings; qualitative evidence only (MS-PS2-5's boundary).
- crash-test-lab (gr 8 lab, concept): contact forces in collisions. Here every force acts without contact.
- cooler-challenge (gr 6 lab, spec): a fair-test bench with A and B samples set side by side. Here the fair test is
  built from a growing table (keep three settings, step the fourth through its values), and the questions start from
  other groups' confounded data.
- warming-evidence-desk (gr 8 data, spec): questions asked of real world records. Here the data is made on the bench.

## Who and how
- Grade 8, science, module Electric and Magnetic Forces (science-8-electric-and-magnetic-forces). Standards:
  MS-PS2-3, MS-PS2-5. Driver: students (solo by default, pairs fine); a teacher can project the class data comparison.
  35 to 50 minutes: Coil 20, Static 8, Field 8, Notebook 6.
- tool.json: driver "students or teacher", minutes "35-50", modes ["Coil", "Static", "Field", "Notebook"],
  grades_label "Grade 8".
- No personal prompts. Nothing is stored except the results table, kept on this device (localStorage
  `curio-emlab`, try/catch) with "Your results stay on this device." under the table (BASELINE rule 7).
- Teacher notes: the model's numbers (clip counts, trial spread, the safety resistor) are a model, labeled so; real
  coils run hot when wired straight to a battery, so switch off between tests; an unpowered steel nail tugs a compass
  needle slightly up close (the model leaves this out; Sam's case 3 uses steel scissors for the same reason).

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-PS2-3 (ask questions about data to find the factors that affect the strength of electric and magnetic forces) | Coil: tap two class data rows, read what differs, add each difference as a question; for each question step one setting through its values with the other three held, three trials each; pick the claim, then the "how much" from their own means. Static: the same for rubbing and gap with balloons A and B | the compare strip ("Groups 1 and 2 differ in Turns and Batteries"), the question board filling, the table rows that belong to the active question lit, the chart of means against the setting, their own ratio in the how-much card | Done 2, 3, 4, 5 |
| MS-PS2-5 (investigate and evaluate a design to give evidence that fields exist between objects not in contact) | Field: drag the compass with the switch off and on, switch off while it is turned, flip the batteries, sprinkle fresh filings after the flip, answer why filings and compass differ. Notebook: find the flaw in three of Sam's tests (two changes at once, touching, no switched-off check) and run each the fair way. Static and Coil: clips and bits jump a gap | the needle swinging with no contact, arrows dropped on the paper, the filing pattern unchanged by a flip while the needle reverses, bits rising across a 2 cm gap | Done 6, 7, 8 |

## Screens and modes
Kit frame, light theme with the tool's own `:root` (Look). Header: "Electromagnet Lab", small line "What makes a magnet
pull harder?" Mode buttons `Coil`, `Static`, `Field`, `Notebook`; kit Motion, Sound, Read.
On load: Coil. Settings 20 turns, 1 battery, Steel nail, Gap 0 cm, switch off, clips in the dish, table empty, board
empty, class data card open. Nothing plays before the first tap. Hint: "Four groups built magnets and got very different
counts. Tap two group rows to see what they did differently." First tap on a group row selects it (main path); first
tap on `Test` runs three trials at once; any other first tap does its own job. The welcome may be cut (BASELINE 16).

Layout at 1366x768, all modes: header 52 px; stage left 64 percent, panel right 36 percent. At 680x425 and 800x500
stage and panel stay side by side (compact panel, buttons first): the backdrop crops, the table shows 2 rows, the chart
folds into a `Chart` button that opens over the table, and the class data card folds into a `Class data` button. At 760
and 375 wide the stage stacks on top at 16:10.

### Coil (opens first)
Focus: the nail tip and the clips while testing; the chart and lit table rows after. Stage: painted bench (em-bench)
top 400 px. On it, side view drawn in code over cutouts: a clamp stand holds the core upright, tip down; the coil is
drawn as N visible wraps of red-enamel wire (10 to 40, pitch shrinks to fit); leads run to a battery holder showing 1 to
3 AA cells (em-aa cutouts), a knife switch (em-switch-open / em-switch-closed), a safety resistor (code, labeled "2.5
ohm resistor"), and an ammeter readout "0.6 A". Under the tip, a dish of 40 clips (em-clip-pile) on a lab jack; a code
ruler shows the gap "Gap 1 cm". Below the bench: results table left (55 percent, 4 rows, `Older`/`Newer`, `Clear
table`) and the chart right (45 percent). Panel top to bottom: hint; class data card (or the claim card when a question
is ready); question board (2 x 2 chips, empty slots read "Ask from the data"); four `.seg` rows `Turns` (10, 20, 30,
40), `Batteries` (1, 2, 3), `Core` (None, Wood, Aluminum, Steel nail, each with a painted swatch), `Gap` (0, 0.5, 1,
2 cm); `Switch` (on/off toggle) and `Test` (big, brand: "Test: 3 trials"); a 44 px `Real one` thumbnail (em-crane).
All above the fold at 1366x768, 1280x720 and 1000x625.
- Class data card: four rows, each a 44 px tap target: Group 1: 20 turns, 1 battery, Steel nail, 0 cm, 6 clips. Group
  2: 40, 2, Steel nail, 0 cm, 24. Group 3: 40, 2, Aluminum, 0 cm, 0. Group 4: 20, 3, Steel nail, 1 cm, 5. Tapping two
  rows shows the compare strip under them and one `Add question` chip per differing setting (Content).
- Chart: the active question's lit rows; x = that setting's values (Core: four categories), y = mean clips (0 to 40, ticks each 10), dots with
  the three trials as small ticks, joined by a line; y label "Mean clips (3 trials)". No question active: empty frame
  with "Tap a question on the board".
- Test: switch closes, the jack lowers, clips leap to the tip and hang as a cluster (count chip "14 clips"), the switch
  opens and they drop; three times, 1.2 s each. Then the row is logged.
- `Real one`: opens a card over the stage: em-crane with "A scrapyard lifting magnet is a coil around iron. Power on:
  it grabs steel. Power off: it lets go." `Close`.
Outcomes on the stage: steel nail lifts a cluster sized by the count (0 to 36), more clips hang as a longer, fuller
cluster; None, Wood and Aluminum lift nothing and show "0 clips" with the clips still in the dish; a gap shows clips
jumping up across it; 0 at a gap shows clips twitching in place (Motion on) and "0 clips".

### Static
Focus: the balloon and the bits. Stage: painted table top (em-table) with 20 paper bits (em-bit-1..3 cutouts) and a
balloon (em-balloon) hanging from a stand; a code ruler shows the gap; a wool cloth (em-wool) at the side. Same table and
chart frame as Coil. Panel: hint; balloon data card (two rows: Balloon A: 5 rubs, 1 cm, 8 bits; Balloon B: 20 rubs, 3 cm,
3 bits) with the same compare and `Add question`; board (2 slots: Rubbing, Gap); `.seg` rows `Rubs` (0, 5, 10, 20, 40),
`Gap` (1, 2, 3, 5 cm); `Test` ("Test: 3 trials"). A trial: the cloth rubs the balloon (0.6 s), the balloon lowers to the
gap, bits leap up and cling (count chip), the balloon is wiped with a damp sponge (caption "wiped: no charge left") and
bits fall. 1.5 s a trial.

### Field
Focus: the compass and the paper. Stage: top-down sheet of paper (em-paper) on the bench, 32 x 20 cm at about 27 px a
cm; the coil drawn in code at the center, axis left to right, 5 cm core; "North" arrow at the top edge ("The paper is
turned so north is up."). The compass (em-compass body, 3.2 cm, needle drawn in code, red north end) starts at the
top left. Panel: hint; checklist (four items, Content); `Turns` and `Batteries` and `Core` (the same settings as Coil,
shared state); `Switch`; `Flip batteries`; `Drop arrow` (drops an arrow at the compass's spot, also key A); `Sprinkle
filings` (clears old filings, draws fresh); `Clear paper`; the filings question card when it unlocks.

### Notebook
Focus: Sam's page. Stage: painted notebook page (em-notebook, 3:4, centered) with Sam's test written in code, and a
small bench picture beside it drawn with the same Coil, Static or Field drawing at 50 percent. Panel: hint; "Case 1 of
3"; the question "What's wrong with Sam's test?"; four option buttons; after a pick the reason, then `Run it the fair way`
(runs the fix on the small bench, result written on the page in a second color as "Fair test:"), then `Next case`.
Case chips 1, 2, 3 at the top let the student move between cases.

## Content
Electromagnet model (Coil and Notebook):
- Current I = batteries x 1.5 V / 2.5 ohm: 0.6, 1.2, 1.8 A (shown on the ammeter). Pole strength P = turns x I x core;
  core: Steel nail 1, None, Wood, Aluminum 0.01.
- Gap factor g: 0 cm 1, 0.5 cm 0.5, 1 cm 0.25, 2 cm 0.06. Mean clips S = 0.5 x P x g. A trial = round(S x (1 + u)), u
  uniform in -0.12 to 0.12, clamped 0 to 40 (seeded per page load; `__tool.seed(n)` for tests).
- Means (steel, 0 cm): 10 turns 3, 6, 9 (1, 2, 3 batteries); 20 turns 6, 12, 18; 30 turns 9, 18, 27; 40 turns 12, 24,
  36. Any non-steel core: under 0.4, always 0 clips. 2 cm gap: 0.18 to 2.16.
- After a lift of 10 or more, switching off leaves 1 clip on the steel tip one time in three, caption "Steel can stay a
  little magnetized."; it falls at the next test.
- Switch held on 10 s or more: caption "The wire is warming up. Switch off between tests." (see Voice warm).
Compare strips (Coil): 1 and 2 "Turns, Batteries"; 2 and 3 "Core"; 1 and 4 "Batteries, Gap"; 2 and 4 "Turns,
Batteries, Gap"; 1 and 3 "Turns, Batteries, Core"; 3 and 4 "all four settings". When 2 or more differ: "These groups
differ in [n] ways, so their counts can't say which one mattered. Add a question and test each on the bench." When one
differs: "Only the core differs, so the core looks important. Test all four cores to be sure."
Questions (chips once added): Turns "Do more turns lift more clips?"; Batteries "Do more batteries lift more clips?";
Core "Does the core change the pull?"; Gap "Does a bigger gap change the pull?"; Rubbing "Does more rubbing lift more
bits?"; Gap (static) "Does a bigger gap lift fewer bits?".
Ready rule: the active question's set = logged rows that match the current values of the other settings. Ready when the
set has: Turns 3 or more values; Batteries 2 or more; Gap (both benches) 3 or more; Core all 4; Rubbing 4 or more
including 40. And it shows a change: highest mean minus lowest at least 2 (Core: steel mean at least 2; Rubbing: mean at
40 at least 6). Not ready because of no change: "Every test in this set lifted about the same. Try a stronger setup:
more batteries or a smaller gap, and test again."
Claims (shuffled, one try, lengths within about 25 percent):
- Turns: right "More turns lifted more clips." Others "More turns lifted fewer clips."; "The turns made no difference to
  the clips."; "Turns helped up to 20, then made no difference."
- Batteries: right "More batteries lifted more clips." Others "More batteries lifted fewer clips."; "The batteries made
  no difference to the clips."; "Two batteries lifted the most; three lifted fewer."
- Core: right "Only the steel nail lifted clips; the others lifted none." Others "Any metal core lifted clips, steel or
  aluminum."; "The core made no difference; the coil did the lifting."; "Wood lifted the most because it is light."
- Gap: right "A bigger gap lifted fewer clips." Others "A bigger gap lifted more clips."; "The gap made no difference to
  the clips."; "Fewer clips at a gap, but only with one battery."
- Rubbing: right "More rubbing lifted more bits, but each extra rub added less." Others "More rubbing lifted more bits,
  and every rub added the same."; "Rubbing made no difference to the bits."; "More rubbing lifted fewer bits."
- Gap (static): right "A bigger gap lifted fewer bits." Others "A bigger gap lifted more bits."; "The gap made no
  difference to the bits."; "Only touching lifts bits; any gap lifts none."
How much (after a right or fixed claim), computed from the student's own means; right = the option nearest their ratio:
- Turns: the tested pair with a whole-number ratio (10 and 20, 10 and 30, 10 and 40, 20 and 40), largest ratio first,
  lower mean at least 4. "From [10] to [40] turns ([4] times as many), your mean went from [3.0] to [12.3]. That is
  about:" options "the same", "2 times", "3 times", "4 times". Batteries: pairs 1 and 2, 1 and 3, same options.
- Gap (coil): base 0 cm mean at least 4; compare 1 cm, else 0.5, else 2. "At [1 cm] your magnet lifted what share of its
  touching count?" options "all of it" (1), "about half" (0.5), "about a quarter" (0.25), "almost none" (0.06).
- Gap (static): base 1 cm mean at least 6; compare 2 cm, else 3, else 5: "all of it" (1), "about half" (0.45), "about
  a fifth" (0.2), "almost none" (0.04).
- No eligible pair: "To compare, test a setting and its double (like 10 and 20 turns, or 1 and 2 batteries), or
  touching (1 cm for balloons), with at least 4 at the smaller count (6 for bits)." (Rubbing has no how much.)
- After the pick: "Your data: [4.1] times. In this model the pull grows in step with turns times current." (turns,
  batteries); "Pull fades fast with distance: a quarter at 1 cm." (coil gap); "About half at 2 cm." (static gap).
Static model: charge share q = 1 - e^(-rubs/10): 0, 0.39, 0.63, 0.86, 0.98. Gap factor h: 1 cm 1, 2 cm 0.45, 3 cm 0.2,
5 cm 0.04. Mean bits = 20 x q x h; trial = round(mean x (1 + u)), u in -0.15 to 0.15, clamped 0 to 20. Means at 1 cm 0,
7.9, 12.6, 17.3, 19.6; 2 cm 0, 3.5, 5.7, 7.8, 8.8; 3 cm 0, 1.6, 2.5, 3.5, 3.9; 5 cm under 0.8.
Field model: Earth's field 1 unit north. Two poles at the core ends (plus or minus 2.5 cm), each 40 x P / r squared
(r in cm), north pole at the right end; `Flip batteries` swaps them. Needle = direction of the sum. Switch off: needle
north. Filings: 1,600 short marks at seeded spots, each drawn along the field with chance min(1, coil field / 3).
Arrows dropped keep their color: brand while on, gray if dropped while off.
Checklist (ticked by the tool, not the student): 1 "Switch off: the needle points north." (compass moved 2 cm or more
with the switch off). 2 "Switch on: the needle turns near the coil." (switch on, needle 30 degrees or more off north).
3 "Switch off again: it swings back." (switch turned off while the needle was 30 degrees or more off). 4 "Flip the
batteries: the needle turns around." (flip while on, needle turns 120 degrees or more). Filings question unlocks after
item 4 and a `Sprinkle filings` press after a flip: "Fresh filings after the flip made the same pattern, but the compass
turned around. Why?" Right "Filings show the field's shape; only the compass shows its direction." Others "The flip
switched the field off, so the filings had nothing to show."; "The flip made the field too weak for the filings to
see."; "The compass is broken; it should have matched the filings." Reason after any pick: "Each filing lines up like a
tiny needle with no north end marked, so a flipped field looks the same. The compass has a north end."
Notebook cases (shuffled options, one try; reason after a wrong pick names the right flaw):
1. Sam: "Test 1: 20 turns, 1 battery, steel nail: 6 clips. Test 2: 40 turns, 3 batteries, steel nail: 36 clips. Turns
   made it 6 times stronger!" Right "Sam changed turns and batteries at once, so the jump can't be pinned on turns."
   Others "Sam should have used a dish with more paper clips."; "Sam should have left a gap in both of the tests."; "Sam
   should have used aluminum, which is lighter than steel." Fair run: 20 and 40 turns, 1 battery: 6 and 12 clips. Page:
   "Fair test: twice the turns, about twice the clips."
2. Sam: "I rubbed a balloon 20 times and pressed it onto the paper bits. They stuck! So an electric force pulls across
   empty space." Right "The balloon touched the bits, so this can't show a pull across a gap." Others "Sam rubbed the
   balloon too many times for a fair result."; "Paper bits are too light to show any electric force."; "Sam needed a
   second balloon to compare it with." Fair run: 20 rubs held at 2 cm: about 8 bits leap up. Page: "Fair test: bits
   jumped a 2 cm gap."
3. Sam: "Compass beside my coil (wood core, 20 turns, 2 batteries), switch on: the needle pointed at the coil. The coil's
   field turned it!" Sam's picture shows steel scissors beside the compass. Right "Scissors sat by the compass and Sam
   never checked it with the switch off." Others "A wood core can't make any field, so the coil did nothing."; "Sam
   should have used three batteries to be sure."; "Compasses only work outdoors, away from desks." Fair run: scissors
   moved away, switch off: north; on: about 45 degrees. Page: "Fair test: off, north; on, the needle turned."

## Interactions in detail
- Any setting change during a Test stops it at once (no row logged; hint "You changed a setting, so that test
  stopped. Tap Test."). Mode switch stops it too. Taps never wait.
- Rows are unique by settings; a retest replaces the row (its cell flashes, "retested"). Table keeps all rows this
  session and on this device; `Clear table` asks "Clear all results?" `Clear` / `Keep`, then clears the board too.
- Only one question is active; tapping a board chip makes it active and lights its set; a ready question shows
  `Answer` on its chip, which opens the claim card in the panel (class data folds to its button). One try: a wrong pick
  shows the reason ("Look at your chart: the mean went up as turns went up.") and the right claim marked; the chip
  reads "tested, fixed". Then the how-much card. A chip reads "tested" or "tested, fixed" when both are done.
- Board stays empty until compares add questions; a question already on the board shows "on the board" in the strip.
  Static's board fills the same way from balloons A and B (differ in Rubs and Gap).
- Switch toggle works outside tests (clips hang while on). Switch on in Field is the same state as Coil's.
- Field: compass drags by pointer or arrow keys (0.5 cm a press); it cannot overlap the coil (stops at the coil's edge).
  Needle eases to its new angle in 0.3 s (instant with Motion off). Max 40 arrows; the oldest goes first.
- Notebook: the fair run is a 3 s animation; `Next case` is live during it. Marks per case: "found" or "found, fixed".
- There is no Reset; a reload keeps the saved table, and `Clear table` is the way to wipe it.
- `window.__tool = {state, setMode, seed(n), coil: {set(k,v), test(), switch(on), compare(a,b), add(q), answer(i),
  howMuch(i)}, stat: {...same}, field: {move(x,y), switch(on), flip(), drop(), sprinkle(), answer(i)}, note: {pick(i),
  fair(), next()}, rows(), allLines, vlog}`.

## Look
Light workbench palette: paper `#f5f3ee`, panel `#ffffff`, ink `#1c2226`, muted `#58626a`, button line `#7d868d`,
focus `#1f5fd1`, ok `#1d7a3c`, warn `#a8321d`. Accent `--brand #0e6b66` (deep enamel teal: Test, chart line, active
question, arrows while on); tint `#e3f1ef` for lit rows. Needle north `#b3261e`; field arrows `#2b5fa8` when gray is not
used; wire enamel `#9a4a12`. Neighbors: cooler-challenge red `#b32630`, which-way-is-down copper `#b4400f`,
warming-evidence-desk amber, bug-hunt mauve, span-and-spire pink, circuit-builder periwinkle on dark, water-shapes-earth
light teal `#58acac` on a dark theme (grade 9; this is a dark teal on light). Contrast (computed): ink 14.50:1 paper,
16.08:1 panel; muted 5.62 / 6.23; brand 5.72 / 6.34, on tint 5.46; white on brand 6.34; north red 5.89 / 6.54; arrow
blue 5.73 / 6.35; wire 5.63 / 6.25; ok 4.85 / 5.38; warn 6.03 / 6.69; focus 5.24 / 5.81; button line 3.34 / 3.71
(non-text). Lit rows also get a left bar; chart dots also carry trial ticks; color is never the only signal.

## Art
Local FLUX, one style: clean painted realism, soft workshop light. No people (`people: false` on all).
- em-crane: "A scrapyard crane holding a crushed gray car under a big round lifting magnet, scrap piles, overcast sky";
  16:9; cutout no; the `Real one` card.
- em-bench: "A tidy school workbench seen from the front, pegboard wall with blank surfaces, warm light"; 16:9; no; Coil
  backdrop.
- em-core-steel, em-core-wood, em-core-al: "a long steel nail", "a smooth wooden dowel", "a smooth aluminum rod", each
  lying flat on white; 4:1; cutout yes; the core in the stand (turned upright) and the Core swatches.
- em-aa: "A plain AA battery with a blank silver and black wrapper"; 9:16; yes; 1 to 3 in the holder.
- em-switch-open, em-switch-closed: "A small knife switch on a wooden base, blade up" / "blade down in the clip"; 4:3;
  yes; the switch.
- em-clip-pile, em-clip: "A small glass dish full of silver paper clips" / "one silver paper clip"; 1:1; yes; dish and
  each clip in the cluster (code places 0 to 40 copies).
- em-table, em-balloon, em-wool, em-bit-1, em-bit-2, em-bit-3: "a light wooden tabletop seen from the front"; "a shiny red
  round balloon with its knot"; "a folded gray wool cloth"; three "small torn scraps of white paper"; 16:9 / 3:4 / 4:3 /
  1:1; table no, rest yes; Static stage.
- em-paper: "A sheet of white paper on a wooden bench, top-down view"; 16:10; no; Field backdrop.
- em-compass: "A round brass compass seen from above with a blank white face and empty center"; 1:1; yes; the compass
  (needle and N mark in code).
- em-scissors: "Steel scissors seen from above, closed"; 4:3; yes; Notebook case 3.
- em-notebook: "An open lab notebook page with faint blue lines, blank"; 3:4; no; Notebook page (text in code).
Code: coil wraps, leads, resistor, ammeter, ruler, jack, needle, arrows, filings, table, chart, all labels.

## Voice
Bank voice `gravel-ranger` (Algenib), restyled "Say warmly with a gravelly voice, like an old shop teacher at a
workbench." (Swapped from easy-coach at the spec check: scarf-juggling-ladder in the same batch uses easy-coach.) Not used by a neighbor (cooler-challenge friendly-dad, warming-evidence-desk friendly-dad, bug-hunt
casual-peer, span-and-spire firm-captain, which-way-is-down upbeat-guide, molecule-forge knowing-guide, circuit-builder
calm-professor, field-lines and collision-lab hs-narrator, gas-law-lab bright-teacher). `Curio.voice`, `scope: () =>
state.mode`. Grade 8: counts, tables and claims are read on screen; no line reads data.
| Key | Kind | When | Stale when | Whole | Text |
|---|---|---|---|---|---|
| wCoil | how | Coil welcome | a compare shown | no | Four groups built magnets and got very different counts. Tap two group rows to see what they did differently. |
| addQ | how | first compare strip | a question added | no | Tap Add question to put that difference on your board. |
| pickQ | how | first question added | a question made active | no | Tap a question on the board, then change only that setting and tap Test. |
| test1 | how | first Test | test ended | no | Three trials, so one odd count can't fool you. Watch the nail tip. |
| keep | how | first logged row while a question is active | ready | no | Keep the other settings the same. Step this one through its values, one Test each. |
| flat | event | a set with no change, once per question | a setting changed | yes | These counts are all about the same. Try a stronger setup, then test again. |
| ready | event | a question becomes ready | answered | yes | You have enough data. Tap Answer on the question. |
| claim | how | first claim card | picked | no | Tap the sentence your chart supports. You get one try. |
| right | event | right pick | next card | yes | Right. Your data backs it up. |
| wrong | event | wrong pick | next card | yes | Not quite. Read why, then look at your chart again. |
| howMuch | how | first how-much card | picked | no | Now look at the numbers. Tap the answer closest to your own means. |
| tested | event | a question marked | mode left | yes | Question tested. |
| warm | how | switch on 10 s | switch off | no | The wire is warming up. Switch off between tests. |
| stopped | how | first test stopped by a change | Test tapped | no | You changed a setting, so that test stopped. Tap Test. |
| wStatic | how | Static welcome | a compare shown | no | Balloon A lifted more bits with less rubbing. Tap both balloon rows to see why. |
| wField | how | Field welcome | item 1 ticked | no | Drag the compass around the coil with the switch off. Watch the red end. |
| item1 | event | item 1 ticked | next item | yes | Points north. |
| item2 | event | item 2 ticked | next item | yes | It turned, and nothing touched it. |
| item3 | event | item 3 ticked | next item | yes | Back to north. |
| item4 | event | item 4 ticked | next item | yes | It turned around. |
| filings | how | filings question unlocks | picked | no | Same pattern, but the needle flipped. Tap the reason why. |
| wNote | how | Notebook welcome | a pick | no | Sam ran three tests, and each one has a flaw. Tap what's wrong with the first. |
| fair | how | first reason shown | fair run tapped | no | Tap Run it the fair way to see what Sam should have found. |
| caseDone | event | a case's fair run ends | next case | yes | That's the fair result. Tap Next case. |
How lines once per page load, then hint only. Events every time, at most once per action; flat at most once per
question per setting change. Read speaks the hint (Coil before any compare: the hint plus the class data summary "Group 2
lifted 24, Group 3 none").

## Family engine
none: no family covers fields or force benches; the tool draws its own coil, needle field, filings, table and one small
line chart in SVG.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Ready gate (fair set) | change two settings at once; test one value; mash Test; random settings | the set only counts rows that match the other three current settings, so a two-change row never joins; 3 values (4 cores) are needed; mashing Test on one setting only retests one row; random wandering that does build a set has built a real fair set, and the gate is not a score |
| Flat-data guard | answer from a set of zeros | no claim is offered until the set shows a change (at least 2 clips or bits apart), so a weak setup cannot give a claim to guess |
| Direction claim | guess; everyday sense ("more turns, more pull"); position; longest; same slot; elimination across questions; the common wrongs (aluminum works, two batteries best, linear rubbing) | one try, shuffled; each question has its own four claims naming its own setting; Core's and Rubbing's right claims go against the common guesses (aluminum is a metal; rubs do not add evenly); a sense guess on Turns, Batteries or Gap only reaches the how-much card, and the question is marked only after it |
| How much | guess; pick "2 times" for any doubling; read the answer off a label | options are ratios, right = nearest to the student's own means (not shown as a ratio anywhere: the card shows the two means and the multiple of the setting, never the clips ratio); the pair varies (2, 3 or 4 times; quarter, half, fifth), so a fixed guess fails; Python: the nearest option matched the model 98.8 percent (turns), 98.8 (batteries), 99.8 (coil gap), 99.96 (static gap); where noise differs, the student's data still rules |
| Answer already on screen | a meter or highlight showing strength | no strength or charge meter exists; the ammeter shows current (the setting, not the result); chart and table show only what the student measured |
| Compare strip | tap rows at random | not scored; any pair adds real questions; Core is reachable only from pairs including Group 3 |
| Field checklist | tap through; drop arrows anywhere | each item is a measured state change (switch, needle angle at least 30 or 120 degrees) the tool detects; there is nothing to tap |
| Filings question | guess; elimination; "compass broken" | one try, shuffled; unlocks only after fresh filings follow a flip, so "filings could not move" is not an option and the student has seen both; guess 1 in 4 |
| Notebook cases | guess; longest; position; pick "change one thing" by habit | one try, shuffled; only case 1 is about two changes, so the habit fails cases 2 and 3; distractors are plausible rule-of-thumb errors; the fair run shows the evidence after |
| Doing nothing | wait | nothing ticks or marks without an action; no timer |

## Heard in order
Grade 8: most text is read, but results land before the next prompt.
- Coil: compare tapped, then addQ (first time); question added, pickQ; Test, test1 (first), the trial animations;
  then flat or ready, whole; Answer, claim; the pick, right or wrong whole, then howMuch; the pick, then tested, whole.
  A tap during a test drops queued how lines, never right, wrong or tested.
- Field: item lines whole, in the order ticked; filings after item 4 and a fresh sprinkle.
- Notebook: wNote; pick, right or wrong whole; fair; the run; caseDone whole before Next case's line.
- The welcome may be cut by the first tap (BASELINE 16); its content stays in the hint and Read.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| A coil's field grows with its turns (B = mu0 n I) | OpenStax College Physics 2e 22.9, solenoid | HyperPhysics "Solenoid" | yes |
| The field grows with the current | same OpenStax 22.9 | same HyperPhysics | yes |
| An iron or steel core makes an electromagnet much stronger; aluminum and wood do not | OpenStax 2e 22.2 "Ferromagnets and Electromagnets" | HyperPhysics "Ferromagnetism" | yes |
| Magnetic pull falls off fast with distance | OpenStax University Physics Vol 2, ch 12 (dipole field) | HyperPhysics "Magnetic dipole" | yes |
| Steel can stay a little magnetized after the current stops | OpenStax 2e 22.2 (permanent magnets from ferromagnets) | HyperPhysics "Hysteresis" | yes |
| An AA cell is 1.5 V; cells in series add their voltages | Energizer E91 product datasheet | OpenStax 2e 21.2 | yes |
| A coil across a battery with little resistance draws a large current and heats | OpenStax 2e 21.2 (internal resistance, short circuit) | HyperPhysics "Joule heating" | yes |
| A compass needle lines up with the magnetic field; alone it points to magnetic north | NOAA NCEI Geomagnetism FAQ | OpenStax 2e 22.1 | yes |
| Reversing the current reverses the field | OpenStax 2e 22.9 (right hand rule 2) | HyperPhysics "Magnetic field of current" | yes |
| Iron filings show a field's shape; a compass shows its direction | OpenStax 2e 22.3 "Magnetic Fields and Magnetic Field Lines" | HyperPhysics "Magnetic field lines" | yes |
| Rubbing a balloon on wool moves electrons and charges it | OpenStax 2e 18.1 | PhET "Balloons and Static Electricity" | yes |
| A charged balloon attracts neutral paper by polarizing it | OpenStax 2e 18.2 | HyperPhysics "Polarization" | yes |
| Electric force grows with charge and falls with distance | OpenStax 2e 18.3 (Coulomb's law) | HyperPhysics "Coulomb's law" | yes |
| Charge from repeated rubbing rises then levels off | Matsusaka et al., Chem Eng Sci 65 (2010) 5781 (exponential approach to saturation) | Lowell and Rose-Innes, Adv Phys 29 (1980) 947 | yes |
| Scrapyard lifting magnets are electromagnets that drop steel when switched off | Britannica "Electromagnet" | HowStuffWorks "How Electromagnets Work" | yes |
| MS-PS2-3 and MS-PS2-5 wording and boundaries (proportional reasoning; qualitative fields) | nextgenscience.org | NSTA NGSS hub | yes |
Backed twice: 16. Cut: "cardboard does not block a magnetic field" (no second source I could name; the barrier toggle is
dropped); the unpowered nail's tug on the needle (left out of the model, a teacher note only); a numeric iron
strengthening factor (shown nowhere). Model values (resistor, clip and bit scale factors, gap factors, trial spread,
iron/air 100:1) are labeled "model" in teacher notes.
Number checks (Python 3, 2026-11-06): all 192 coil settings tabulated (max 36 clips; every non-steel setting under 0.4,
always 0); 20,000 random fair Turns sets: when the gate opens (13,863), no set had means going down; how-much with
nearest option: turns 21,586 cases, 1.2 percent where the student's nearest differs from the model, batteries 1.2
percent, coil gap 107 of 48,006, static gap 17 of 41,936; ratio within 0.5 of the model's whole number missed 3 percent,
so "nearest to own data" was chosen; static: 40,000 sets each for rubbing and gap, none reversed end to end, 1.7
percent show a small dip between 20 and 40 rubs (the levels-off claim still holds); levels-off gate (4+ values with 40,
mean at least 6): 27,031 sets, first slope larger in all; field: iron 10 turns 1 battery turns the needle 86 degrees at
6 cm and 10 degrees at the paper's corner (18 cm); air core 40 turns 3 batteries 63 degrees at 6 cm; air 10 turns 1
battery 9 degrees at 6 cm and about 45 at the coil's edge, so item 2 is reachable with every setting; case 3 fair run 45
degrees; flipped field reverses the needle at all four test points.

## Done when
1. Focus and one idea: tapping Groups 1 and 2 shows "Turns, Batteries" and two `Add question` chips; testing 10, 20,
   40 turns at 1 battery, steel, 0 cm lights three rows and the chart rises; Answer, the right claim, then the how-much
   card gives "4 times" from the student's own means.
2. Ready gate: a row with two settings changed never lights; a set of zeros gives the flat line and no Answer.
3. Each of the six claims marks right only for the listed sentence; Core needs all four cores tested.
4. How much: right equals the option nearest the student's ratio, for turns, batteries and both gaps; small counts get
   "too small to compare".
5. Static: balloons A and B add Rubbing and Gap; rubbing claim needs 4 values with 40; bits jump a gap on the stage.
6. Field: the four checklist items tick only by the actions listed; the needle points north with the switch off and
   turns near the coil with it on; flip reverses it; fresh filings look the same before and after a flip.
7. Notebook: three cases, one try each, fair runs give 6 and 12 clips, about 8 bits at 2 cm, north then about 45 degrees.
8. A tap on any setting during a test stops it at once with no row logged; Field and Notebook taps act at once.
9. At 1366x768 every mode's stage, all setting rows, `Test` and the board sit above the fold; at 680x425 stage and panel
   stay side by side with the chart and class data in buttons.
10. Voice: how lines once each; right, wrong, ready and tested whole before the next prompt; no line names a disabled
    or hidden control; results table says it stays on this device.
11. No people in any art; no network requests; no console errors.

## Open questions
None.
