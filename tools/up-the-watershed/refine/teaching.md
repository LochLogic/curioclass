# Teaching lens: up-the-watershed (round 1)

Cold read of spec.md, src.html, notes.md, tool.draft.json, voice/lines.json, the shared audit
(S:/CurioClass-codex-scratch/up-the-watershed/audit-r1) and my own drives in
S:/CurioClass-codex-scratch/up-the-watershed/teaching/frames (drive.py, port 9891). Not a Curiosity; judged as a
grade 12 lesson tool.

## Findings

1. **Claim mode, src.html:1230-1260 and 1225, 1569. An empty claim gives away every culprit and the answer key.**
   Opening Beach closed, pressing Claim and pressing Submit claim with nothing checked and zero kits used returns
   "Missed source. Look for beach closed evidence after a storm near pasture. / Missed source. The storm drains only
   flow in storms. / Missed source. Look for a dry-day jump below town." That names all three culprits. The same
   submit unlocks Show the whole creek, which draws every suspect's percent share (Green lake, zero samples: plant
   86.7 dry, fields 27.2 and construction 23.4 storm). Then "right source, but evidence does not bracket it" names
   the exact spots and weather to sample. A student can solve every case by following instructions without ever
   choosing a sampling stop, which is the one idea of the tool ("the case is about sampling strategy").
   Seen: frames/empty-submit.png (feedback text captured), frames/empty-submit-reveal.png. Better: Submit needs at
   least one checked suspect with evidence attached; a missed source gets a location-free nudge ("Something else
   adds most of the storm-day E. coli here; you have not sampled where it enters"), not its name; Show the whole
   creek waits until the kits are spent or the case is solved. **Level: blocker. Tag: family:hidden-information
   (general lesson: a submit with nothing in it must not return the key).**

2. **Claim rule and notes "Key skills", src.html:775 (wClaim), 1592; notes.md "Key skills". The culprit rule cannot
   be computed from anything the student sees.** The Claim hint (also spoken) says "Check sources with at least 20
   percent at an over-limit target". Shares depend on load = concentration x flow, but no flow appears anywhere on
   screen (result card, logbook and compare show concentrations only; the spec's flows, 0.30 / 1.80 m3/s etc., are
   builder-only). So the student guesses "big jump" and the 20 percent line is only ever learned from the feedback or
   the reveal. The notes claim the key skill "Distinguish concentration, load and dilution", but load is never shown
   or asked for, and the dilution case (S5 storm 1,626 after mixing two forks; S7 storm E. coli rising less than the
   Pipe's 5,000 suggests) is never made visible as load. Seen: grep of src.html for flow output; frames/empty-submit-reveal.png.
   Better: put flow on each result card and logbook row (m3/s) and a load line in Compare two ("load up 13.3 billion
   CFU/s from S6 to S7"), so the 20 percent rule is checkable; or drop the key skill and restate the rule as
   something observable. **Level: should fix. Tag: general.**

3. **Map, src.html:643 (`M810 421L612 470`). The storm drain line joins the creek below the Main Street bridge (S7),
   but the model adds the storm drains above S7.** S7 is drawn at (560, 483); the drain line ends at (612, 470),
   downstream of the S7 bridge (M530 475 L585 457). The model (src.html:859-862), the spec and the evidence rule
   (D1 bracketed by S6 and S7) all put the drains above S7. A student reading the map would bracket the drains with
   S7 and S8 and be told the evidence does not bracket it. Bracketing from the map is the core skill, so the map must
   agree with the model. Seen: frames/crop-pipe.png (crop of empty-submit-reveal.png). Better: end the drain line on
   the creek between the Old sewer and the S7 bridge. **Level: should fix. Tag: general.**

4. **Evidence check, src.html:1176-1189. Attaching every logbook sample to every suspect passes.** validEvidence only
   asks whether the needed pair is somewhere in the attached set; unrelated samples are ignored. With eight beach
   samples attached to Pasture, Storm drains and Old sewer, all three return valid (drive check `dump`:
   {"A":true,"D1":true,"D2":true}). The notes' key skill "Support a claim with a direct sample or a bracketing pair"
   is not tested. Better: evidence that includes samples not on that suspect's reach gets "right source; trim the
   evidence to the pair that brackets it", or the attached set must be the pair (plus at most the contrast pair for
   D1). **Level: should fix. Tag: general.**

5. **Fix-it gauges, src.html:1449, 1458. The meter bar is a fixed 35 percent for any missed goal and the goal text
   disappears after Test plan.** Width is `met ? 100 : 35`, so a lake plan at 0.214 and one at 0.051 look the same.
   After testing, the caption under Lake and Creek is replaced by "Storm concentration 0.290 mg/L P." and "Dry
   remains 9.1 mg/L.", so the target ("Dry P < 0.05; storm load -25%", "cut at least 50%") is no longer on screen
   while students compare. Seen: audit-r1/state-fix-tested-1366x768.png. Better: fill toward the goal (for example
   percent of the needed cut achieved) and keep the target line under the detail. **Level: should fix. Tag: general.**

6. **notes.md "The modes", last two paragraphs. Builder change notes leaked into the teacher notes.** "Use Fix
   details to read every intervention's effects and who pays, including on phones and short previews. The claim
   instruction states the 20 percent source rule before students submit." and "Field photographs preserve the whole
   scene, including the cattle's feet in the creek." read as fix logs, not teacher guidance. Better: cut them, keep
   the useful fact (whole-creek shares count only upstream sources; the plant adds nothing at Main Street) as one
   plain sentence. **Level: should fix. Tag: general.**

7. **Muddy creek card, src.html:714; Model notes 1595. The sediment band is cut short.** EIFAC (1965) has a fourth band:
   over 400 mg/L "at best only poor fisheries". The case value is 481, so the honest label is the over-400 band, not
   "Over 80: unlikely good fisheries". Checked against the EIFAC Technical Paper 1 band table (four bands: under 25,
   25 to 80, 80 to 400, over 400). Better: "Over 400: poor fisheries at best" on the card, and list all four bands
   in Model notes. **Level: polish. Tag: general.**

8. **Missed-source hint wording, src.html:1257.** "Look for beach closed evidence after a storm near pasture." and
   "Look for green lake evidence..." splice the case title into the sentence. (Moot if finding 1 removes names.)
   **Level: nit. Tag: general.**

9. **tool.draft.json sources.** Lists both "Eight retained illustrations drawn with FLUX.1-schnell" and "Illustrations
   generated with OpenAI gpt-image"; the spec says local FLUX only. One of these is wrong about where the art came
   from. Craft should confirm which. **Level: nit. Tag: general.**

## Done when (spec)
1. Sample values: pass. The model run in the page (`__tool.model`) reproduces every row of the Sample table to the
   listed rounding (S4 dry 26.7 shows as 27, S8 dry 1,357.5 as 1,358).
2. Beach in 8 kits with D2 (S6, S7 dry), A (S1, S2 storm), D1 (Pipe storm): pass by code (5 kits).
3. Geese: "About 9 percent dry, 5 percent storm" and wrong: pass (src.html:1249; shares 8.9 / 5.4 recomputed).
4. Green lake: Outfall alone catches the plant; fields and construction need storm pairs: pass.
5. Muddy creek: C with S5 and S6 storm solves; B gives "only 14 percent": pass (audit claim-solved state).
6. E + D2 + A + C + G: $2,955,000; 64.0 / closed (461.5); 0.041, 26.5 percent; 228.4, 52.5 percent; all met: pass.
7. Seven-fix plan: lake 0.209 dry, fails: pass.
8. Every fix: $4,100,000, Test plan disabled: pass by code (src.html:1429).
9 to 12 are layout and voice; the audit's size and walk rows are clean for them and Play and Craft own them.

## Facts checked
Recomputed in the page: every Sample table value, every case share in the spec, and the worked plans (E alone 0.047 /
7.3 percent; C alone 260.2 / 45.9; C + A 431.5 / 518.5 and 52.5; D2 + A 64.0 / 461.5; + D1 321.7). All match.
Reference values checked against their sources: E. coli 126 GM and 410 STV CFU/100 mL (EPA 2012 RWQC), nitrate-N
10 mg/L MCL, total phosphorus 0.05 mg/L for streams entering lakes (EPA Gold Book 1986), EIFAC sediment bands (see
finding 7), EPA 841-B-03-004, 841-B-05-004, 832-R-08-006, NRCS 382 (fence), 390 (riparian herbaceous cover), 605
(denitrifying bioreactor). Correct. (Water troughs are NRCS 614, not cited; harmless.)

Standards: HS-ESS3-4 is exercised by testing and revising fixes against measured goals in Fix-it. HS-ETS1-3 is
exercised by the $3 million budget, who-pays lines, saved plans and the Why box. Both real; the Why box is not
saved or checked, which is fine for a classroom discussion.

Grade fit and guardrails: grade 12 language is right. No hard history, health or cultural content; no sensitivity
review needed. Support at home ideas are doable tonight and say not to enter the water.

## Audit pilot
- Leads confirmed: none of the audit's leads are teaching leads; its clean rows (sizes, walks, motion) are cited
  for Done when 9 to 12.
- Leads wrong: none checked from this lens.
- What it missed: the empty-submit giveaway (finding 1), the uncomputable 20 percent rule (2), the map drawing the
  storm drain below S7 (3), the evidence dump (4), and the fixed-width gauge bar (5). All are meaning problems a
  mechanical audit cannot see.
