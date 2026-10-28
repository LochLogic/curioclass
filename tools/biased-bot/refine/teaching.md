# Teaching lens: biased-bot (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json; bundled with
`CURIO_DRAFT=1 python scripts/bundle_tool.py biased-bot` (177 KB). Audit first (`scripts/audit_tool.py`, ports
9960-9961), then `scripts/drive.py` with held clicks and real pad drags on port 9962, own profile. Numbers recomputed
in Python from the spec alone (own mulberry32, templates, card generation, 32 by 32 rasterizer, k = 3 vote with
position tie-break; a reversed training order gives the same table). Scratch: lens-bb-teaching (calc.py, sweep.py over
all 1330 jar settings, pad.py; frames f1 to f7, audit/).

Counts: blockers 0, should fix 4 (general 3, family 1), polish 2 (general 2), nit 2 (general 2).

## Standards (rule 2)

Module computer-science-4-training-data-matters: "How training data shapes what an ML model outputs".

- **E4-ALG-ML-02**: taught by doing. The student changes whose cards are in the jars, presses Train Bitsy and reruns
  the same 30 cards; the room bars and Mix-ups show what changed. Taught, but S2 lets a solo student skip the "more of
  the same does nothing" half.
- **E4-SOC-HU-18**: taught. The bars are split by room, so the student sees the harm land on Room 9 and fixes it by
  including Room 9's writing; 0 / 15 / 0 lets a solo student move the harm onto the other rooms (line 7 plays). S1
  weakens the "look at how they write" step.
- **E4-DAT-IM-11**: taught by the controlled comparisons (same test cards, one jar changed per run, results by group).
  The "predict" half exists only as hint text with nothing to commit to (P1).
- **E3-ALG-ML-02**: taught in Try Your Writing: label your own drawing, Bitsy retrains, the look-alikes and later reads
  change. Real, but S3 makes the first try look like it did nothing.
- CSTA crosswalk and AI4K12 are reference only; 1B-DA-07 has the same gap as P1.

No code is only mentioned; none needs to move.

## Done when

| # | Result | How checked |
|---|---|---|
| 1 | pass | held Run, Skip: 10 / 10 / 6; Mix-ups "Room 9: wrote 1, got tacos (4), 4 cards" (one row with its count, as the spec's panel describes); Python: four Room 9 1s read as 4 (f1 dw1-run) |
| 2 | pass | 30 / 0 / 0 retrained: 10 / 10 / 6; vlog: three results, "under", then "More cards from the same rooms did not help Room 9." spoken (f5 v2-same) |
| 3 | pass | Room 9 at 3: 10 / 10 / 6, no "all" line; at 6: 10 / 10 / 10 and "Every room got the right lunch..." spoken (f6) |
| 4 | pass | 0 / 15 / 0: 6 / 6 / 10, eight 1s read as 7 (salad), "Now a different room is getting the wrong lunch." spoken (f5 v4-flip) |
| 5 | pass | More Room 3 after a run: Run aria-disabled, "Old results. Train Bitsy, then run again.", box greyed (f1 dw5-old) |
| 6 | pass, see S3 | real drag of a stick 1: "Bitsy reads: 1", 16 ink cells, three Room 12 look-alikes with badges (f7 w1-stick). Flag 1 drag reads 4; It's a 1 once: still 4; twice: 1, look-alikes My cards, My cards, Room 12 (f7 w2-flag) |
| 7 | pass | grayscale frames: circle / square / triangle plus "Room N" on jars, bars, cards and viewer (f1 dw7-gray, dw7-gray-bars) |
| 8 | pass | audit frames 680x425, 1366x768, 760x900 and 375x812 host: Run, Train Bitsy and all six jar buttons above the fold |

## Facts and numbers

All eight rows of the spec's checked table and the notes' table match my Python exactly, including the notes' mix-up
detail ("Room 9 loses two 1s to 4 and three 4s to 1" at 3 / 0 / 0; four 1s per other room read as 7 at 0 / 15 / 0).
Results do not depend on training order. Two My cards labelled 1 (flag style) also fix Room 9 in the lunch line
(10 / 10 / 10), which the tool shows correctly (f7 w3-flag-run). The Gender Shades citation and summary (highest error
for darker-skinned women, binary gender classification, PMLR 81, 2018) are right; the numeral-style claim matches the
cited Wikipedia section; the screen names no real place or group.

## Findings

**S1. should fix, general. "Tap a room's jar to see how its students write" leads to an empty jar.**
(src.html `L.under`, `openViewer`; notes "A 5-minute start" step 3.) After the first run the voice and hint say to tap
a room's jar, and notes step 3 says "Tap the Room 9 jar. Compare its 1 with Room 12's 1." But Room 9's jar starts at
0, so the viewer says "This jar has no training cards yet." and "This jar is empty. Press Close, then More to add
cards." (f1 dw1-under-jar9). The key framing line ("Lots of people learn to write 1 with a long flag...") only shows
once Room 9 has jar cards, so a student who looks first, as told, never sees it. Same after 0 / 15 / 0: the rooms now
getting wrong lunches are the empty jars. Better: an empty jar's viewer shows that room's 10 lunch-line cards ("Room
9's lunch cards. Bitsy has none of these in its jar.") with the framing line for Room 9; or point the line at the lunch
cards on the stage. Fix notes step 3 to match.

**S2. should fix, general. After a run the hint does not name the next experiment.** (src.html `nextHint` -> 'ready'.)
After every run the hint goes back to "Press Run the lunch line. Predict how many right lunches each room will get."
(f1 dw1-run), that is, rerun the same jars, which teaches nothing. The tool's one idea is the contrast: more Room 12
cards change nothing, a few Room 9 cards fix it. A solo student (rule 4) who goes straight to Room 9 never meets the
first half; line 5 only plays if they happen to add Room 12 or Room 3 cards first. Better: a post-run hint when a room
is under 10 that names the experiment and the control, e.g. "Room 9 got wrong lunches. Press More under Room 12. Will
more of the same cards help?", then after that run "Now try More under Room 9." (how lines, once each, `V.heard`).

**S3. should fix, family:ml-lab. The first "Teach Bitsy my way" visibly does nothing, with no reason given.**
(src.html `teach`, hint 'taught'.) A flag-style 1 reads 4; It's a 1 once, then Bitsy, read it!: still 4, because the
student's card is one of three votes against two Room 12 4s (Python: 200 of 200 fresh flag-1 drawings still read 4
after one taught card; 200 of 200 read 1 after two). The screen says "Bitsy learned your card." and then gets it wrong
again; a grade 4 student concludes teaching is broken. Only the teacher notes explain it. Better: after a teach that
does not flip the read, show the vote in the look-alikes ("Your card is 1 of the 3 look-alikes. Bitsy goes with the
most votes. Teach one more.") so the k = 3 vote becomes part of what E3-ALG-ML-02 teaches. Family lesson: any k > 1
tool needs the vote visible when one example can't win it.

**S4. should fix, general. "Bitsy learned from everyone" is false in the state that triggers it.** (src.html `L.all`,
spec voice line 6.) Done-when 3 reaches all 10s at 15 / 6 / 0, with Room 3's jar empty. Two My cards also trigger it
with no Room 9 cards at all (f7 w3). The table's point is that Room 3 needed no cards of its own because it writes the
same shapes; "learned from everyone" teaches the opposite. Better: "Every room got the right lunch. Bitsy has now seen
every way these numbers are written." (lines.json and the clip change with it).

**P1. polish, general (spec open question). The predict step has nothing to commit to.** Hint 'ready' says "Predict
how many right lunches each room will get", but a solo student can't record a guess, so the prediction half of
E4-DAT-IM-11 / 1B-DA-07 lives only in a teacher question. A quick guess per room, shown beside the bars after the run,
would make it something the student does. It adds a control, so it goes to the spec's open questions.

**P2. polish, general. The "one Room 9 card is not enough, two are" talk point needs its condition.** (notes Talk
about it, bullet 4; spec talk points.) True with Room 12 at 15 and Room 3 at 0, but the sweep finds all 10s with one
Room 9 card of each digit (6 / 3 / 6, 3 / 3 / 9, 0 / 3 / 9), and 3 / 6 / 0 hurts Room 12 (8) and Room 3 (7). Say "with
Room 12 at 15 and the other jars empty" in the notes so a teacher isn't caught out by a pair that found one of these.

**N1. nit, general. The empty-jar viewer says the same thing twice** ("This jar has no training cards yet." and "This
jar is empty. Press Close, then More to add cards.", f1 dw1-under-jar9). Moot if S1 is fixed.

**N2. nit, general. Teaching a card also trains untrained jar changes.** `teach` retrains on `state.counts` and clears
`dirty`, so jar changes made without Train Bitsy get trained silently from the writing mode. Use `state.trained`.

## Giveaways, language, guardrails

- No hidden-information or quiz mode; nothing before a run shows its result. Badges are drawn but never features
  (features are the 64 cells only). Nothing to solve by sweeping; the sweep is the activity.
- Language is plain grade 4 on screen ("Right lunch = Bitsy reads the written number correctly."). Notes name the
  sensitive context (rule 8).
- Grade 4: no K-2 or hard-history guardrails apply.

## For the sensitivity agent (rule 5, not judged here)

Room 9 stands in for people who learned a different numeral style (the cited source ties it to much of Europe and
Latin America), and the tool's arc is a group harmed by being left out of the data. Notes also carry the Gender Shades
parallel (skin tone and gender). Worth a fresh sensitivity read of the Room 9 framing and that teacher note.

## Audit pilot

- Confirmed: sizes clean at all eight sizes (my Done-when 8 check agrees), Motion off clean, and the held-click walk's
  spoken lines (jar clicks speak 'inspect' / 'inspectEmpty', More / Fewer speak 'change').
- Wrong: all 11 leads at 375x812 are false. They are panel content scrolled out of view inside the 350 px
  `overflow:auto` panel (result label, bars, notes) counted as overlapping the stage text below it.
- Missed (all teaching, all past one click): the empty Room 9 jar behind the post-run line (S1; the walk logged
  "This jar is empty" for #jar-9 with no way to judge it), the post-run hint (S2), the first teach doing nothing (S3),
  the false "learned from everyone" (S4), every number, and whether the Done-when lines play (needs multi-run
  sequences).
- Tooling note: in my drive.py runs a shot's `"wait"` did not let page timers run (a real Run click, then a 31 s
  `wait`: 0 of 30 cards done, and the result lines looked stuck after the first). Awaiting inside the `"after"` JS
  worked. Voice counts taken across a `"wait"` should be read with care.
