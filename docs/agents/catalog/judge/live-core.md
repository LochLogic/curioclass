# Judge report: the 27 live math, ELA and science tools (2026-11-10)

Judge pass for the catalog review (docs/agents/CATALOG-REVIEW.md, step 3). Read: the adoption bar, BASELINE rules 1,
2, 4, 13, 14, 20, the review plan and pilot results, the extract brief (row format 2), VISION, both pilot judge files,
the 27 rows, SPEC.md, STANDARDS.md, REFINE.md (Teaching lens), docs/TOOL-CONTRACT.md, and for six tools the notes,
plan, tool.json, spec where present and greps of src.html. The other 21 are judged from their rows plus spot greps;
where a line rests on the row alone it says "(row)". Read and report only. Nothing else was changed.

## Headlines

1. The rows are mostly a true finding, not a harsh test. Of 63 code entries, 1 is "taught" (35 practiced, 24 shown, 3 touched). The early tools were
   built to an "explore first, challenges optional" rule (SPEC.md), and that rule is what the new test catches.
2. The test is too harsh in two places: it calls honest iteration "beating the check", and it has no label for a
   sound "see why" tool. Two wording changes fix both (end of part A).
3. The catalog is the right raw material. 4 tools meet the bar now, 7 are right for their job, 14 need a fix (10 of
   them small), 2 carry the wrong code. Nothing needs a rebuild.
4. The bigger gap is not inside the tools. 18 of 27 rows sit on a module whose cluster holds standards the tool never
   touches, and 25 of the 26 modules have one tool. Examples: 8.EE.C.7 (solving equations, major work of grade 8),
   6.NS.B.2 and B.3, 2.MD.7, all of L.2.1, W.2.1 and W.2.3, seasons in MS-ESS1-1.
5. Fix the small ones before more are built, and change six rules so the next 700 do not repeat the pattern.

## A. Cold check of six rows

I worked out what the student does from the files and src.html first, then opened the row.

| Tool | What the student really does | Row | Verdict on the row |
|---|---|---|---|
| nonsense-words | Reads made-up words aloud in 8 patterns (CVC, silent e, digraphs, blends, vowel teams, diphthongs, r-controlled, endings); a partner taps Right or Not yet. The tool never says the word and has no model of blending. | RF.2.3a practiced, check teacher, beatable "tap Right" | Right on depth, wrong on reach. A partner's ear is the only honest check for reading aloud with no microphone, so "beatable" is unfair here. The row codes one standard; the tool also practices RF.1.3a to c, RF.2.3b and RF.2.3d. Too harsh on the check, too narrow on the codes. |
| corner-store | Taps each coin to count the payment (or presses Count it together and watches). For change, adds coins from the drawer; a flag over every change coin shows the running total from the price and turns red past the amount paid. The clock moves by itself. 9 customers: 3 exact, 6 with change. | 2.MD.8 practiced, 2.MD.7 shown | Right, and a little kind. The row caught "too much, too little" but missed the running-total flags: the tool does the counting up on screen, so the child only has to add coins until the flag matches. 2.MD.7 "shown" is fair; nothing asks the time. |
| smoothie-lab | In Orders, works out a scaled recipe and sets the scoops, 7 orders, one of each kind (scale up, fill to a total, use what is left, simplest form, party batch, percent, unit rate). A miss says which fruit is too much and both percents; a hint comes after two misses. The ratio table and line appear after the order is right. | All five codes practiced or shown; "nudge to green" beatable | Right on 3a (the tool makes the table) and on ratio words (never asked). Too harsh on 6.RP.A.3: the student does the key step, with a guide and a real key. The true weakness is one problem per kind, and a miss message that points the way. "Taught in part, thin" would be the honest label, and the scale cannot say it. |
| moon-phase-model | Drags the Moon and the time, sees space and backyard views of one instant, turns on tilt to see why eclipses are rare. Predict: sees a backyard Moon, drags the Moon in space to where it must be, one check, answer shown. No seasons anywhere. | MS-ESS1-1 practiced; seasons missing; Predict passes about 3 in 8 by chance | Right. "Use a model" is done by the student; "develop" and "describe" are on paper. The missing seasons (a third of the expectation, with no other tool on the module) is the real finding and the row has it. |
| collision-lab | Sets masses, speeds and bumpers, launches, records runs to a notebook that plots momentum before against after on a y = x line, and writes four conclusions. In Crumple Zone, picks a nose, sets crush force and length, launches, reads the force graph, tries again; a spec sheet sets limits, one of which cannot be met. | HS-PS2-2 practiced, HS-PS2-3 practiced; "slide until it says met" beatable | Too harsh on both. HS-PS2-2 asks students to use math to support a claim: recording runs and reading them against a line is that practice. HS-PS2-3 asks them to design, evaluate and refine: trying again after a launch is the standard, not a way round it. The row itself says in `unsure` that both would be taught under a looser reading. This tool meets the bar. |
| ferris-wheel | Ride: sets radius, hub, turn time; the tool draws the curve and writes h(t). Unit Circle: steps the angle, presses One radian and Unroll. Match (marked "optional challenge" in the spec): sets sliders until the curve lands on a dashed target; a miss names the biggest gap. | F-TF.A.1 shown, A.2 practiced, B.5 practiced, C.8 shown | Right on B.5 (the tool writes the equation and Match is optional). Fair but blunt on A.1: it is an "understand" standard and the bent rod is a good way to see it, yet the student only presses a button. Too kind on C.8: a readout of 1.000 is not proving or using the identity; that is `claimed`. |

Score: of 15 code labels in these six, I agree with 10, call 4 too harsh (collision-lab 2, smoothie-lab 6.RP.A.3,
nonsense-words on its check) and 1 too kind (ferris-wheel C.8). One more outside the sample: three-pigs-lab has
2-PS1-2 as "touched", but testing materials for a job is what the child does there; 2-PS1-1 (classify) is the weak one.

**Verdict on row format 2.** Sound, and far better than format 1: `parts_missing`, `key_step` and `on_path` carried
the real findings on every row. Keep it. Two wording changes:

1. **Narrow `beatable`, and say what is not beating.** "A check is beatable only when trial is cheaper than thinking:
   fewer than about six choices, or feedback that says which way to move, with free tries. Trying again is not beating
   when the standard itself asks for it (design and refine, investigate, revise). For reading aloud, a partner or
   teacher marking is a real check, not a hole."
2. **Judge `key_step` by the standard's verb, and add a depth `explored`.** "If the verb is understand, interpret,
   use a model, observe or investigate, the key step is setting up cases and saying what will happen. `explored`: on
   the main path, the student sets up the cases, meets every part of the idea, and predicts before a reveal or checks
   against a shown guide. Fill `unit_adds` with what a unit or sheet must then supply. If the verb is solve, write,
   compute, prove or model, `explored` is not allowed: the tool doing it is `shown`." Pressing a button to watch
   (ferris-wheel One radian, how-animals-see) stays `shown`, so weak tools do not slip through.

Also: one tool that practices more codes than its spec names should have them listed (add a field `codes_unclaimed`).

## B. The 27 tools sorted

"Small" is a fix pass, "medium" a new mode or step set, "large" a rebuild. No tool is large.

**1. Meets the bar as a tool now (4)**

- **hundred-hop:** counting aloud is an oral standard; the hidden pads and Reveal are a real class check for K
  (row). K.CC.A.3 (writing numerals) is paper work; name it on the module.
- **size-of-everything:** 8.EE.A.3 taught: one try per pin, ten items, real size sense. 8.EE.A.4 arithmetic is shown,
  not done; a sheet carries it. The module still needs a tool for 8.EE.A.1 and A.2.
- **undo-machine:** the student builds the inverse chain over escalating levels with a real verdict; the swap trick
  only works on the first two-card levels (row). The strip writes the formula, so a sheet adds "write g(x)".
- **collision-lab:** the student does the practice both expectations name (see A). Polish only: turn Predict on by
  default and lead from Crumple Zone into the spec sheet.

**2. Right for its job; the unit adds the rest (7)**

- **poll-workshop:** S-IC.B.4 names simulation, and this is one. Unit adds: experiments and observational studies
  (S-IC.B.3), a written inference, margin of error by hand. Move S-ID.A.4 off (a toggle only).
- **imaginary-island:** shows why multiplying by i turns and why roots leave the real line (N-CN.B.4, B.5). Unit
  adds all hand arithmetic (N-CN.A.2) and solving (N-CN.C.7); those two codes should name a sheet, not this tool.
- **rollercoaster-polynomials:** zeros, multiplicity and end behavior seen from the building side. Unit adds
  factoring to find zeros and hand division. Move A-APR.C.4 off (nothing is proved).
- **nonsense-words:** a sound practice station with no guess prompts. The unit adds the taught phonics lesson and the
  order of patterns. List the codes it really practices (grade 1 and 2).
- **melt-or-not:** predict, test, sort is right for a teacher-led K-2 class. Unit adds the "because" sentence (a
  frame on a sheet). 2-PS1-3 on the module has no tool.
- **habitat-hunt:** observing and comparing kinds across four places is the practice. Unit adds a real schoolyard
  look and saying the comparison. Tiny fix: Compare should wait until a scene is finished.
- **three-pigs-lab:** tests materials for a job (2-PS1-2). Unit adds the class chart and sorting by property
  (2-PS1-1), which the plan already does with real samples.

**3. Needs a targeted fix worth doing now (14)**

| Tool | The gap | Fix | Size |
|---|---|---|---|
| two-trains | 8.EE.C.8 is major work; Yard has no goal, Dispatch (optional) carries the standard, the student never writes an equation; card 7 passes on one button | Lead from Yard into Dispatch; boxes for the meeting time and place before Check on every card; fix card 7 | medium |
| smoothie-lab | 6.RP.A is major work; one order per kind; tool makes the table; miss message points the way | 3 or more orders per kind (generated); student fills two blank table cells; miss says only "does not taste the same" on the first try | medium |
| corner-store | Running-total flags do the counting up; 2.MD.7 claimed, never asked | Hide the change flags until Give change (keep them for the first change customer as the model); either ask "what time is it now?" with three clocks, or drop time from the outcome | small |
| marching-band | Tool pairs, totals and writes both equations; the call is a coin flip (row) | Hide the sentence and total until the class answers; let the child tap the pairs on some rounds | small |
| factor-forge | Melt computes GCF and LCM; the distributive part of 6.NS.B.4 is absent (row) | Type the GCF and LCM before Melt shows them; one "36 + 8 = 4(9 + 2)" round set | small |
| sight-words | Lists mix regular and irregular words and drill them all as wholes, which is the practice the K-2 reading bar warns against; list licence not checked (row) | Tag the truly irregular words, show the tricky part on the card, route regular words to decoding; check the list licence | small |
| hamburger-paragraph | W.2.2 is writing; the child sorts given sentences; Write your own counts parts only | Put Write your own on the path after two burgers, with an on-screen self-check (names the topic, two facts, an ending) | small |
| contraction-crusher | Crush with nothing tapped shows the answer; the tool places the apostrophe; no possessives | After the first model, Crush needs a mark; the child drops the apostrophe in the gap; possessives go to another tool | small |
| moon-phase-model | Seasons are a third of MS-ESS1-1 and absent; Predict is loose | A seasons view (tilt, sun angle, day length) with its own predict; tighten Predict to half a phase and ask why | medium |
| how-animals-see | Three expectations, all watched; 1-in-5 quiz | Student builds the light path (Sun, object, eye) for 4-PS4-2 and picks the structure that explains a view for 4-LS1-1; move 4-LS1-2 off (no brain or response step) | medium |
| field-lines | HS-PS2-4 says "describe and predict"; nothing is predicted (row) | A Predict toggle: type the force change before doubling a distance or charge, then compare | small |
| outbreak-model | Tool writes every log step; Guess first is unscored (row) | Hold the log steps until the guess is in; score the guess within a tolerance | small |
| ferris-wheel | F-TF.B.5 lives in optional Match and the tool writes h(t); C.8 is a readout | Lead from Ride into three Match targets where amplitude, midline and period are typed before the curve shows; move F-TF.C.8 off | small |
| savings-plan | Derivation is clicked through; using the formula is optional; cents can be nudged (row) | One fill-in step in the derivation; lead into Plan Desk; cap tries or ask for the computed deposit once | small |

**4. Wrong code or wrong grade (2, plus codes to move from tools above)**

- **motion-graph-match:** a fine tool for position, velocity and acceleration graphs. HS-PS2-1 is about force, mass
  and acceleration data, and here force is one readout at a fixed mass. Keep the tool as the kinematics lesson; give
  HS-PS2-1 to a tool where the student varies force and mass and reads the data.
- **elements-inspector:** a Curiosity (not scored on curriculum value). It has no plan and no predict step, so by
  VISION's own rule it should be the second card on its module; HS-PS1-1 needs a lesson tool beside it.
- **Codes to move off a tool that only displays them:** F-TF.C.8 (ferris-wheel), A-APR.C.4 (rollercoaster-polynomials),
  S-ID.A.4 (poll-workshop), 4-LS1-2 (how-animals-see), 2.MD.7 (corner-store, unless the clock step is added),
  N-CN.A.2 and N-CN.C.7 (imaginary-island, to a sheet).
- **Codes to add:** nonsense-words practices RF.1.3a to c, RF.2.3b and RF.2.3d; it is a grade 1 to 3 tool on a grade
  2 module.

## C. Patterns, and the rule that would have caught each

What the weak cases share:

1. **The mode that carries the standard is optional.** Dispatch, Match, Plan Desk, Clue Trail, Write your own, the
   spec sheet. SPEC.md told the writer to do this: "Challenges are optional modes, never the point."
2. **The tool does the verb.** It writes the equation, makes the table, counts up, pairs, melts, plots, concludes.
   The old spec had no place to say who does the step; REFINE's Teaching lens asks only that a code is "really
   taught by something the student does", with no test by parts.
3. **Feedback that walks the student to the answer.** "Too much strawberry", "biggest gap near t = 35", a running
   total, a live checklist. Good teaching feedback, but it turns a check into hot and cold.
4. **One problem per skill.** Seven orders for five codes; one unit-rate item; one percent item.
5. **A readout counted as a code.** An identity line, a normal-curve toggle, a force arrow.
6. **A cluster on the module, one standard in the tool.** The module code says 6.NS.B or L.2.1; L.2.2; the tool
   teaches one line of it and nothing owns the rest.
7. **The explaining and writing live only in plan.md**, so a student alone (rule 4) never meets them.

Rule changes (at most six):

1. **SPEC.md, Rules, "Explore first":** exploring opens the tool, but the mode that carries a "do" standard is on the
   main path, and the first hint after exploring leads into it. *Not in the new format; the old line is still there.*
2. **SPEC.md, Standards map:** each row quotes the standard's verb and lists its parts, and names who does the verb;
   if the tool does it, the code moves or the design changes. *Partly there: the map asks for a student action and a
   check, not the parts or who does the step.*
3. **SPEC.md, Standards map:** each "do" code has at least five checked items that differ, and each "understand" code
   has a predict before the reveal. *Not there.*
4. **SPEC.md, "Can it be beaten?":** add to the list "feedback that says which way to move" and "a readout or
   running total that already shows the answer", and say that trying again is fine where the standard asks for it.
   *Mostly there: "the answer already on screen" is listed; hot and cold feedback is not.*
5. **REFINE.md, Teaching lens item 1:** test every code part by part and name who does the key step, and a code that
   lives only in an optional mode, a readout or plan.md is a blocker. *Not there.*
6. **docs/TOOL-CONTRACT.md and data/modules.csv:** a module lists standards, never a bare cluster; tool.json's
   `outcome` claims only what the student does on the main path and carries a `role` (lesson, see why, practice) with
   one line on what the unit adds. *Not there; the pilot found the same cluster problem.*

STANDARDS.md needs no change; the gap is in the spec template and the Teaching lens.

## D. Direction

**Right raw material, fixable gaps.** The tools are well made, the facts hold, and the "see why" moments (equal
ratios look the same, the crossing is a place and a time, the lit half always faces the Sun) are what paper cannot
do and what reviewers mean by understanding. What the bar would mark down is narrower: the tool often stops one
step short of making the student do the thing, and leaves that step to a teacher who may not be there. That is a
last-step problem, not a wrong direction. The newer spec format already closes about half of it.

**What a single tool should be held to.** A tool is one lesson's centerpiece, so it owes one standard (or one clear
part of one), done properly. A testable definition:

> A tool teaches a standard when a student alone, following only the tool's own lead, (1) meets a model or worked
> case, (2) does the standard's own verb on every part of its wording, on at least five items that differ, (3) is
> checked by something where thinking is cheaper than trial, and (4) none of that sits in a mode they could skip.
> For an "understand" standard, (2) is: sets up the case and predicts before the reveal.

Left to units, worksheets and the Reading Room: fluency volume, long writing and explaining, talk, hands-on work,
using the idea in a new setting, and reading that builds knowledge. A tool should say in one line which of these
it hands on, so the unit writer does not have to find out.

**One tool per module is not enough for major work.** A module like grade 4 fractions, 6.RP or 8.EE.C holds three
to seven standards and weeks of class time; the bar asks that most of the year goes there. Today those modules get
the same single tool as a one-standard supporting topic. I would give major-work modules two or three tools: one
"see why" tool, one "do it" tool with generated problems and a real check, and where needed one for use on story
problems. Depth inside one tool (more modes) is second best, because optional modes are the very thing that failed
here. What to trade: build fewer new tools on supporting and additional clusters for now, and let worksheets carry
fluency, which they already do well. It also means splitting cluster modules into standard-level modules first, so
the gaps show on The Map instead of hiding behind one tool.

**Fix before more are built, in this order.**

1. The six rule changes (a day of doc edits; they shape every tool after).
2. Major work, K-8: two-trains, smoothie-lab.
3. K-2 reading risk: sight-words.
4. The cheap ones that close a "tool does it" hole: corner-store, marching-band, contraction-crusher,
   hamburger-paragraph, factor-forge, field-lines.
5. Science with a missing part: moon-phase-model (seasons), how-animals-see.
6. Grade 11 small fixes: ferris-wheel, outbreak-model, savings-plan.
7. Code moves (group 4 list) with scripts/add_codes.py, and open concepts for the standards left bare: 8.EE.C.7,
   6.NS.B.2 and B.3, 2.MD.7, L.2.1, W.2.1, W.2.3, 2-PS1-3, HS-PS2-1, HS-PS1-1.

The ten small fixes are about one Refine pass each. Doing them now also gives the builders ten worked examples of
the new rules, which is worth more than the fixes themselves.

## Limits of this report

- Six tools were checked in src.html. The other 21 rest on the rows; lines marked "(row)" should be confirmed by the
  fix agent before it changes anything.
- Standard wordings are from memory, not checked against the published text.
- I did not check which bare standards are already carried by live worksheets; some of the gaps in D.7 may be.
