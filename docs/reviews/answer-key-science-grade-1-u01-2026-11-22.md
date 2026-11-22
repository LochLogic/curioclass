# Answer-key read: science-grade-1 unit 1 (2026-11-22)

Kind: answer-key. Target: science-grade-1-u01, the end-of-unit assessment items (check = end). Unit 1 has no
check or mid items; the three end items s01-E1, s01-E2 and s01-E3 are the whole scope. Course finish, COURSE-RUN
stage 7. Read-only: nothing edited but this report.

## What I studied

The answer-key read studies by solving. I solved each item cold from its stem in data/plans/science-grade-1/items.csv
and the picture spec in courses/science-grade-1/u01-2/sheets-day7.md, writing my own answer and evidence, before
opening the answer, samples, wrongs.csv rows, the sheet keys or the unit plan.

- s01-E1 (mine): tree to roof to hill; at 3 p.m. lower above the hill; evidence sheets 1 and 2 (sheet 3 does not show
  the covered place).
- s01-E2 (mine): pole to barn to ridge; at 11 a.m. lower above the ridge; evidence sheet 4 (sheet 5's two shown
  places agree with it and could fairly be circled too); the morning moon is a real moon.
- s01-E3 (mine): stars; evidence the two clear dark night records; the day records show stars are not seen in a
  bright sky (circling them too is defensible).

Then read: the item answers, samples and steps; the six wrongs.csv rows for these items; courses/science-grade-1/u01-2/d007.md,
sheets-day7.md, response-sheet.md and key-cards-sky-day-night.md; docs/courses/science-grade-1/s01.md (standard,
limits, section 5 assessment table and scoring).

## Verdict

Pass with fixes. All three keys match my cold answers and each item tests the 1-ESS1-1 goal the unit plan names (sun
path, moon path, stars at night and not by day, within the stated limits); the fixes are one plan-versus-key evidence
mismatch, a teacher pointer to the wrong key file, and one garbled key sentence.

## Findings

1. **s01-E2, evidence: unit plan and key disagree (item ambiguous).** s01.md section 5, item M: "lower above ridge,
   using sheets 4 and 5." items.csv steps: "circles sheet 4 as the evidence"; answer: "sheet 4 shows it." A child who
   circles 4 and 5 is following the plan and is fairly right (sheet 5's pole and barn places agree with the path).
   Fix: in items.csv s01-E2 steps, write "circles sheet 4 as the evidence; circling sheets 4 and 5 also meets", and
   add the same clause after "from sheet 4" in the sheets-day7.md key line. Leave the plan wording as it is (it
   already accepts both).

2. **d007 points the teacher to the wrong key.** d007.md Before class: "Key: key-cards-sky-day-night.md." That file
   keys the day 5 sky cards (cards 1, 3, 5, 7; card 8 cloudy), not E1 to E3. The E1 to E3 keys sit only at the foot
   of sheets-day7.md. Fix: "Key: the keys line at the foot of sheets-day7.md; key-cards-sky-day-night.md keys the
   waiting children's card sets."

3. **s01-E3 answer, garbled sentence.** items.csv answer: "The empty day records are not seen in the bright sky, not
   gone." The records are not what is unseen. Fix: "On the day records the stars are not seen in the bright sky; they
   are not gone."

4. **s01-E1 and s01-E3, a fair extra circle (minor, item ambiguous).** E1: a child may circle 1, 2 and 3; E3: a child
   may circle all four records (the day records are part of the pattern too). The steps name only sheets 1 and 2 and
   only the night records, so the teacher has no rule. Fix: add to each steps cell "an extra circle on the covered
   sheet (E1) or on the day records (E3) still meets, if the named ones are circled."

Checked and sound: each stem and the day 7 sheets show every place and time the key needs (low, high, lower over three
fixed landmarks, clock pictures); invented-for-practice labels are on the sheets and said aloud; the moon times are
plausible as different days (plan: clock times differ, no fixed daily moon time); wrongs.csv codes A to D match the
plan and d007's notes, and D is noted, not scored, as the plan says; no item steps past the limits (no rotation,
orbits, phases).

## Gate

plan.py check, filtered: science-grade-1: 240 items, 369 wrong answers, 13 failures, all "section N.N
(science-grade-1-uNN-N) is not in data/units.csv", none from these items.

## Could not settle

None.

## Fixes applied (2026-11-22)

1. s01-E2: applied. Step accepts circling sheets 4 and 5; same clause in the sheets-day7.md keys line.
2. d007 key pointer: applied. Before class points to the keys line at the foot of sheets-day7.md.
3. s01-E3 answer: applied. "On the day records the stars are not seen in the bright sky; they are not gone." Keys line matches.
4. s01-E1 and s01-E3 extra circle: applied. Each step accepts the extra circle; the keys line says so.
