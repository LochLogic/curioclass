# Expert read: Social and Emotional Learning frames, Grades 3 to 5, 6 to 8 and 9 to 12 (2026-11-25)

One combined cold read (docs/pipeline/briefs/frame-read.md, after-core changes) of the three SEL band frames written
2026-11-25 on the pattern of the fixed K to 2 pilot. The reader did not write them.

## What was read

- AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/sel.md; docs/pipeline/briefs/frame-read.md and the
  "After-core courses" part of frame-write.md.
- The frames: docs/courses/social-and-emotional-learning-grades-3-to-5/frame.md, -6-to-8/frame.md, -9-to-12/frame.md
  (course in brief, Seams, Models carried, Units, Course-level checks, Cross-subject, For the lead), and the K to 2
  pilot frame's seams and Models carried.
- data/progressions/sel.csv (520 rows), data/plans/frames.csv (the four SEL rows), data/plans/calendar.csv.
- docs/courses/sel/STANDARD.md section 7 ("Shared steps"); DESK-ANSWERS q-fix-sel-1 and the 2026-11-25 band-frame
  entry; docs/reviews/frame-social-and-emotional-learning-grades-k-to-2-fixes-2026-11-25.md (pattern notes).
- The health and PE frames of each band, at their SEL lines and tables (health-grades-3-to-5, -6-to-8, -9-to-12;
  physical-education-grades-3-to-5, -6-to-8, -9-to-12); the computer science grade 5, 6, 7, 11 and 12 frames
  (existence and the team-project lean).
- Checks run: `frame.py check` on all three (0 failures each; 60 unit days a year, 180 or 240 in units, 12 or 16
  check and respond days), `progression.py check sel` (520 rows, 0 failures), `stale.py check` (1 failure, PE 9 to 12
  line 387, a Pending on the SEL 9 to 12 frame). A script parsed each Units table against sel.csv: every grade 3 to
  12 row is placed in exactly one unit of its year, no unit carries a row of another grade, and every seam table cites
  the right unit for all 40 rows on both sides of each band edge (3 to 5 and K to 2, 6 to 8 and 3 to 5, 9 to 12 and 6
  to 8).
- No outside source was fetched (no downloads); the court and archive pages the frames cite were not opened.
  Confidence on each finding rests on the repository and the lens, marked below.

## Verdict

All three frames are sound in their data: every owned row is placed once, unit sizes follow q-fix-sel-1 exactly
(four of 11 and two of 10 a year, grades 4 and 5 of 3 to 5 using STANDARD section 2's moved session), the days add to
64 a year, the checks sit clear of core check weeks and days, and the seam tables agree across every band edge.
Cases are invented throughout, sharing is optional, checks score a character's step and never a student's feeling,
and no real-child disclosure is asked for. The biggest risks are cross-band: the 9 to 12 frame rewords the shared
I-statement instead of growing it, and one historical case (Brown v. Board of Education) is used in four years across
three bands, twice inside 6 to 8. The one change that matters most is fixing the I-statement wording before any 9 to
12 unit plan builds its card.

Per frame: **3 to 5** sound, minor fixes (numbering seen from health, check load, stale notes). **6 to 8** sound
with two moderate fixes (Brown twice; card lineage from 3 to 5 lost, so grade 6 calls 3 to 5 cards new). **9 to 12**
sound once the I-statement is fixed (one serious), plus stale computer science notes.

Count: 14 findings: 2 serious, 4 moderate, 5 minor, 3 judgment calls.

## Findings

### Serious

**S1. The 9 to 12 I-statement is reworded, not grown (9 to 12 frame lines 13, 137, 148; sel.csv g9-rel-friendships).**
LAYER frame, progression. REPEAT new. Confidence: firm (STANDARD section 7 and both earlier frames agree).
What is wrong: STANDARD section 7 sets one set of words across SEL, health and PE; the 6 to 8 frame hands on "I feel
___ when ___ because ___. I need ___." The 9 to 12 frame says it "adds a request and a check-back" but writes
"when..., I feel..., I would like..., does that work for you?": the order changes, "because" and "I need" drop out.
Its own Leave-out bullet still calls it "the four-part I-statement frame". Nine units use the card (4, 6, 8, 10, 16,
17, 18, 22 to 24). Why it matters: a writer builds a new card with new words, so a grade 9 student meets a third
I-statement after health's and 6 to 8's, the exact fault the shared-steps rule was written to stop (lens: "a skill's
name or steps changed"). Fix: in the 9 to 12 frame (course in brief "Shared steps", Models carried row, unit 4 What
students learn) and sel.csv g9-rel-friendships, use "I feel ___ when ___ because ___. I need ___. Does that work for
you?" (the 6 to 8 frame kept, the check-back added as a fifth part; "I need" is the request); the Leave-out bullet then
says "the five-part I-statement frame".

**S2. Brown v. Board of Education carries SO6 in four years across three bands, twice inside 6 to 8.**
LAYER frame. REPEAT new. Confidence: firm (lens "Errors reviewers catch", first line; 9 to 12 For the lead 11 names
the risk). What is wrong: Brown is the settled-history case in grade 5 (3 to 5 unit 15), grade 7 (6 to 8 unit 9),
grade 8 (6 to 8 unit 16) and grade 10 (9 to 12 unit 9). The 6 to 8 frame uses the same case in two consecutive years
of its own band; 9 to 12 picked four distinct cases and asked the earlier bands not to reuse them, but did not
reserve Brown. Why it matters: a grade 8 student meets the same page and the same question a year after grade 7; the
lens names a year that repeats another year's cases as a frame error, and depth cannot grow on a case the class
already knows the answer to. Fix (settled below, item-level): keep Brown in grade 5 (it sits beside social studies
grade 5 unit 9, the natural home) and in grade 10 only if the 9 to 12 frame says it is a deliberate return at new
depth; otherwise 9 to 12 unit 9 takes another settled case. In 6 to 8, grade 7 unit 9 takes the Nineteenth Amendment
(1920, a settled change to who could vote) and grade 8 unit 16 takes a settled disability-access change (Section 504
of the Rehabilitation Act, 1973, or the Americans with Disabilities Act, 1990), each from a federal archive page the
sensitivity agent reads first; the 6 to 8 course in brief, units 9 and 16, Sensitivity reads and For the lead 11 change
to match.

### Moderate

**M1. Unit numbers for SEL differ between SEL and its neighbors (health 3 to 5 SEL table; sel.csv notes).**
LAYER frame, process. REPEAT new. Confidence: firm. What is wrong: the SEL frames number units through the band
(grade 4's calm-down unit is unit 10), but sel.csv's notes start each year at "Unit 1", and the health 3 to 5 frame's
SEL table copies that ("g4-sm-calm-down (SEL unit 4)", "g5-sm-calm-down (SEL unit 1)"), while PE 3 to 5 uses band
numbers ("SEL unit 11"). A teacher or writer opening the SEL 3 to 5 frame at "unit 4" finds grade 3's "When friends
disagree". In 9 to 12 the shared ground is one-sided the other way: health 9 to 12 numbers no SEL unit and PE 9 to 12
still holds a Pending on this frame (stale.py fails it). Why it matters: the brief's rule "each names the other" is
met only from the SEL side, and a writer following health's pointer builds a retrieval on the wrong unit. Fix: the
lead (health and PE sides are the lead's) writes band numbers with the year beside them in health 3 to 5's SEL table
("SEL unit 10, grade 4"), names SEL units 1, 2, 4, 6, 10 and 17 in health 9 to 12, and rewrites PE 9 to 12 line 387
from the SEL 9 to 12 frame; sel.csv notes keep year numbers (the scope is written a year at a time) and the SEL
STANDARD section 3 says so in one line, so every reader knows which numbering a note uses.

**M2. The widened Check session is over-full in 3 to 5 and 6 to 8, and the item counts disagree with the rule.**
LAYER frame. REPEAT new. Confidence: likely (reasoning on the minutes; no source). What is wrong: the course-level
check is the unit's Check session widened with sampled items (allowed by frame-write, "A course-level check right after
a unit"). The 3 to 5 rule says "one or two items sampled", but its cells name three (grade 3 year-end, grade 4 and 5
mid-year) and some add a sampled rehearsal ("the four calm-down steps done on the card"); the 6 to 8 section sets no
cap and its cells name four or five sampled items (grade 6 mid-year, grade 7 year-end) beside a three- or four-item
end-of-unit page and a watched rehearsal per pair, all in about 20 minutes of a 30-minute session. Why it matters: a
writer builds a page a grade 3 or grade 6 class cannot finish while the teacher also watches up to 15 pairs, so the
last pairs are marked in a rush or not at all. Fix: in both frames state the cap once ("at most two sampled items,
written only; sampled steps are never a second rehearsal") and trim each check cell to two sampled items; the 9 to 12
frame (40 minutes, two items in every cell) already meets this and is the model.

**M3. The 6 to 8 frame loses the 3 to 5 card lineage, so grade 6 calls grade 3 work new (6 to 8 Models carried; sel.csv
g6-rel-stand-up, g6-rel-ask-offer-help).** LAYER frame, progression. REPEAT yes (the same kind as the row-change items
the 3 to 5 writer flagged). Confidence: firm. What is wrong: the 6 to 8 Models carried lists the refusal options card
and the upstander options card as "new in this band", but 3 to 5 unit 5 teaches a four-step refusal and an upstander
plan with four options (g3-rel-stand-up), and 3 to 5's own Models carried omits both cards, so the lineage breaks on
both sides. The row changes applied today landed in part: g6-sa-name-feelings and g6-sm-calm-down now grow the 3 to 5
forms, and g6-rel-stand-up opens with "the grades 3 to 5 upstander plan gains report online", but its step-up clause
still reads "from one planned speak-up to a choice among upstander options", which grade 3 already does.
g6-rel-ask-offer-help's step-up ("choosing the helper that fits the size of the problem") is grade 3's problem size
meter (each level with who to go to). Why it matters: grade 6 writers build these as first-teach days, repeating
grade 3 at the same depth (lens: a sub-skill met again with no new depth). Fix: add the refusal steps and the upstander
plan to 3 to 5 Models carried (grown in unit 5, used in 11 and 16 and 17); in 6 to 8 Models carried move both cards
out of "new in this band" into rows that say what grade 6 adds (refusal: the option that fits the place; upstander:
"report online"); rewrite the two step-up clauses ("from the four-option plan offline to the same plan with a report
online and the safest option chosen for a team chat"; "from the helper that fits a size to the helper that fits a
place and a channel in a school of many adults").

**M4. Health 3 to 5 and SEL 3 to 5 each claim the shared I-statement, in different words.** LAYER frame. REPEAT yes
(the K to 2 read's health seam finding). Confidence: firm. What is wrong: health 3 to 5's SEL section says the courses
use "one I-statement (health's words ... Please ___.)"; SEL 3 to 5 and STANDARD section 7 say "I need ___". Both are
taught in grade 3 weeks 17 to 21 (health unit 4, SEL unit 4). SEL For the lead 4 (a) names the fix, but neither frame
says which wording a writer uses today. Why it matters: grade 3 gets two cards in the same weeks. Fix: the lead applies
For the lead 4 (a) in health 3 to 5 ("I need ___"), and until then both frames carry one line, "Pending: health takes
STANDARD section 7's wording", so a writer does not pick.

### Minor

**m1. Stale "not written" and "being written" notes.** LAYER process. REPEAT yes (K to 2 read finding 14).
3 to 5 line 124 ("The grades 6 to 8 frame is being written beside this one"); 3 to 5 line 305 and For the lead 5
("Computer science grade 5's frame is not written": it is, and g5-team-project sits in its unit 3); 3 to 5 For the lead
5's PE Pending notes (stale.py no longer fails PE 3 to 5, whose seam now names SEL units); 6 to 8 For the lead 8
("computer science grades 6 and 7 are not written": both are); 9 to 12 lines 272 to 281 and For the lead 8
(computer science grades 11 and 12 "not written": both are); 9 to 12 For the lead 12 (the joint read of the 6 to 8
Handed on and 9 to 12 Picked up tables is done here: all 40 rows agree). Fix: rewrite each to what is true, citing the
computer science units where a lean exists.

**m2. The "judgement" spelling change did not land.** LAYER standard. REPEAT new. 6 to 8 For the lead 4 lists "Snap
judgements" to US spelling "also in STANDARD section 3"; STANDARD.md still has "judgement" at lines 100, 132, 154, 157
and 216 (the lens, line 37, too). Fix: "judgment" in all six places.

**m3. One calm-down step changes its word between bands.** LAYER frame. REPEAT new. 3 to 5 (and PE 3 to 5) teach
"stop, breathe, name it, choose"; 6 to 8 (and PE 6 to 8, 9 to 12 Picked up) grow it to "stop, breathe, name it, pick a
tool, go on", so "choose" becomes "pick a tool". Fix (settled below): grade 6 keeps "choose" and adds "go on": "stop,
breathe, name it, choose, go on", in the 6 to 8 frame, sel.csv g6-sm-calm-down, the 9 to 12 Models carried row and PE
6 to 8's cue lines.

**m4. The 9 to 12 claim "every unit of the year is sampled twice" is not true.** LAYER frame. REPEAT new. Units 3 and
6 of each year are the checks themselves and are not sampled again in the year; units 1, 2, 4 and 5 are sampled once.
Fix: "every unit is checked by its own end-of-unit assessment, and units 1, 2, 4 and 5 are sampled once more in the
year's checks; units 3 and 6 (and the year's last unit) return in the next year's retrieval openings".

**m5. Partner customs are named by kind only, against the pilot's pattern note.** LAYER frame. REPEAT yes (K to 2
Codex read 7). The pilot fix asked that "game sources [be cited] at frame time". 3 to 5 units 3, 9 and 17 name only
the kind of custom (scoring or turns, a meal's work, how a group decides) and defer place and source to the unit
plan; 9 to 12 units 3, 9, 16 and 22 do the same. Fix: either name one source per unit now (with "browser check" where
it blocks), or say in each frame's Base text that the unit plan names it and the sensitivity read checks it, and drop
the "distinct from PE's and arts' picks once those are written" clause, since those frames are written: check them now.

### Judgment calls

**J1. 3 to 12 fold the course-level checks into Check sessions; K to 2 does not.** LAYER frame. REPEAT new. 3 to 12
keep q-fix-sel-1's sizes exactly and widen the unit's Check session; the K to 2 pilot uses 11 and 8 and separate check
sessions, a departure still on Cory's desk (its For Cory 1). Both are legal under frame-write. The bands now differ in
shape, which is fine (the 20-minute K to 2 session cannot hold a widened check), but the K to 2 For Cory card should
say that 3 to 12 kept 11 and 10 by folding, so Cory picks with the whole picture. No change to these frames.

**J2. Grade 6's depth is "a choice among options" in about 35 of 40 rows.** LAYER progression. REPEAT new. It follows
STANDARD's 6 to 8 ladder rung ("a choice under real pressures"), but read across the year it is one formula; combined
with M3 it invites grade 6 days that only lay out options. Reviewers could differ. Pick: leave the rows, and ask the
grade 6 scope writer to name the pressure in each Application (onlookers, an online pull, a deadline), which the rows
already hold.

**J3. 3 to 5 grades 4 and 5 run three two-group units before the mid-year check.** LAYER frame. REPEAT new. This moves
one session to a twelfth unit so the check clears core weeks; it is allowed (STANDARD section 2) and the groups fit
(no two-group unit holds more than six rows). Pick: accept.

## Clashes for the lead's calendar pass (not counted)

From data/plans/calendar.csv, same grade and week, SEL check or respond against another after-core check or respond:

- Grade 3: week 11 (SEL respond) with computer science grade 3's check; week 26 (SEL year-end check) with dance,
  media arts, visual arts, PE and computer science checks; week 27 (respond) with theater, computer science and ELD.
- Grade 4: week 15 (check and respond) with music, ELD, health's respond and library's respond; week 26 with dance,
  theater and PE.
- Grade 5: week 15 with music, health's mid-year check and library's respond; week 26 with dance, visual arts, PE and
  computer science's respond; week 27 with theater.
- Grade 6: week 16 respond beside math grade 6 (different school days: SEL 78, math 80; no day clash). Grade 7: week
  16 respond with computer science grade 7's check. Grade 8: week 16 with career exploration and library checks.
  Weeks 32 in grades 6 to 12 are finals weeks, shared by rule.
- Grades 9 to 12, week 15 or 16: grade 9 with library (15), health, PE and biology (16); grade 10 with computer
  science, career pathways and library (15 and 16) and PE (16); grade 11 with PE (16); grade 12 with library (15),
  ELD and PE (16).
- No SEL check falls on a core check school day in grades 6 to 8 (checked by day).

## What is right and should not be touched

- Row placement: every grade 3 to 12 row in exactly one unit of its year, matching sel.csv's unit notes; the seam
  tables agree on all 40 rows at each band edge.
- Sizes and days: q-fix-sel-1 kept, short paths keep every unit, 64 sessions a year, check weeks clear of core checks.
- Inside-the-session budgets (5, 20, 5 at 30 minutes; 5, 28, 5, 2 at 40) and the cap of three new sub-skills per
  Understanding session.
- Sensitivity: invented students and families, "real or made up" sharing, private pages for SA4, SA7 and SA9, no
  student asked about a move, loss, family or culture, the teacher or a card playing every unkind or pushing part,
  health named for every topic it owns, and the 18-or-over line in 9 to 12.
- Leave-out bridges listed card by card in every frame.

## What it could not judge

- The court, archive and museum pages (Brown, Mendez, Morgan, Heart of Atlanta) were not opened; whether each is
  taught "as settled fact with dignity" waits on the sensitivity agent's read.
- Whether a 30-minute widened Check fits in practice (M2) rests on reasoning; a timed probe of one unit plan would
  settle it.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| 9 to 12 I-statement: "I feel ___ when ___ because ___. I need ___. Does that work for you?" | Grows the 6 to 8 card by one part, keeps STANDARD section 7's words | 9 to 12 frame; sel.csv g9-rel-friendships |
| 6 to 8 settled cases: grade 7 unit 9 the Nineteenth Amendment (1920); grade 8 unit 16 Section 504 (1973) or the ADA (1990) | No case twice in a band; Brown stays in grade 5 | 6 to 8 frame |
| Grade 6 calm-down steps: "stop, breathe, name it, choose, go on" | Keeps the 3 to 5 word "choose", adds one step | 6 to 8 frame; sel.csv g6-sm-calm-down; 9 to 12 Models carried; PE 6 to 8 (lead) |
| Sampled items in a widened Check: at most two, written only | Fits the 30-minute session; 9 to 12 already does it | 3 to 5 and 6 to 8 Course-level checks |
| Seam tables 6 to 8 Handed on and 9 to 12 Picked up: agree, no change | All 40 rows checked by script | none |

## For Cory

1. **Grading or credit for SEL 9 to 12** (scope; 9 to 12 For the lead 9): whether a school may give credit for the
   advisory course.
2. **Supply ceiling** (money): none is set; the three frames price about $55 to $60 a year printing plus small
   supplies (9 to 12 up to about $20 a pilot).
3. **Unit sizes across bands** (scope; K to 2 For Cory 1): 3 to 12 kept q-fix-sel-1's 11 and 10 by folding the checks
   into Check sessions; K to 2 alone uses 11 and 8. Pick: accept both shapes.
