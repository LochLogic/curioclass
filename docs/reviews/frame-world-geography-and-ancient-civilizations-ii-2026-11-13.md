# Frame read: World Geography and Ancient Civilizations II (grade 7), 2026-11-13

Reader: the curriculum expert (docs/agents/EXPERT.md), cold. Brief: docs/pipeline/briefs/frame-read.md.

## What I read

- docs/courses/world-geography-and-ancient-civilizations-ii/frame.md, in full; its row in data/plans/frames.csv
  (12 units, 160 days). No base text, so no source map.
- The 29 grade 7 rows of data/progressions/social-studies.csv, every column; the grade 6, grade 8 and grade 9 rows
  they take from or hand to (assumes and hands_on checked both ways by script: no broken pair).
- The neighbour frames: world-geography-and-ancient-civilizations-i (before) and civics-government-and-civic-life
  (after). No World History I frame exists yet.
- The bar: docs/agents/lenses/social-studies.md, docs/ADOPTION-BAR-SUBJECTS.md (shared core and section 1),
  docs/courses/social-studies/STANDARD.md, docs/FOUNDATION.md section 7, the MA.7 lines of
  data/standards/ma-hss-2018.txt, the C3 ids.
- Every cross-subject row named in the frame, and every ELA, math and science row that names an ss7 row. No grade 7
  ELA, math or science frame exists yet.
- Earlier reads: the 2026-11-13 social studies and cross progression reviews; no earlier frame read.
- Gates: `python -X utf8 scripts/plan.py check` (this frame: 0 failures, 12 units, 148 days in units, 12 for
  checks); `python -X utf8 scripts/stale.py check` (0 failures). I counted the MA.7 codes by hand: 58, as the frame
  says. Unit day windows in the cross-subject table match the unit days.

## Verdict

The frame is sound: all 58 anchor codes and the grade 7 C3 indicators are placed, the regional order is the anchor's
with each departure named, and the year's skills climb well (objects with no readable script, a ruler's edicts,
ranked causes, two secondary works compared, an argument naming the opposing claim). The biggest risk is unit 4: it
lists bronze, silk, paper and gunpowder under the Qin and leaves the Han dynasty a "candidate", though the anchor's
own Silk Roads standard is a Han story and gunpowder is 1,000 years after the Qin; a writer would build wrong days
from it. The one change that matters most is to name the Han inside MA.7.T2b.2f and date each technology; next, the
human reads list.

## Findings

### 1. Unit 4 dates China's technologies wrongly and leaves out the dynasty its standard needs

- **What is wrong.** Unit 4's cell reads "The First Emperor and the Qin: ...; bronze, silk, paper and gunpowder".
  Bronze casting belongs to the Shang (taught in unit 3), paper to the Han (about the 2nd century BCE, improved
  about 105 CE), and gunpowder to the Tang (9th century CE), after this course ends at about 500 (from memory; the
  row's own "and later paper and gunpowder" shows the writer knew, but the frame drops "later"). And MA.7.T2b.2f
  (China's part in Silk Road trade, and Buddhism reaching China from about the 1st century CE) is the Han's: Zhang
  Qian's missions west, Han trade with Parthia and Rome, Buddhism's arrival under the Han. The frame keeps the Han
  only as a check-set candidate.
- **Why it matters.** A day writer builds a Qin day that credits the First Emperor with gunpowder, an error C3(a)
  fails, and teaches 2f without naming the state that made the trade, so the standard is taught in part (C1).
- **Fix.** Unit 4 cell: "the Qin (221 to 206 BCE): conquest, Legalism, one set of weights, coins and script, forced
  labor; then the Han (206 BCE to 220 CE): the Silk Roads opened west, Buddhism arriving; China's technologies on
  the timeline with their dates (bronze from the Shang, silk, paper under the Han, gunpowder under the Tang as a
  pointer past this course)". Same words in ss7-qin-unification and ss7-silk-road-trade notes. Drop the Han from
  "Check set adds" and "For the lead" 2: it is part of 2f, not an addition (see "Settled by the expert").
- LAYER frame and progression. REPEAT new. Confidence: firm on the dates (well established, from memory); likely on
  2f needing the Han.

### 2. The human reads are fewer than the bar and FOUNDATION require

- **What is wrong.** "Units 2, 6, 8 and 10 need the fresh-agent sensitivity read, and unit 6 a qualified person's
  read." Bar item 12 asks the read of every unit; FOUNDATION section 7 asks a reader from the community concerned for
  hard-history content. Units 2 (caste and discrimination against Dalits), 8 (slavery in Athens, Sparta's helots)
  and 10 (Roman slavery) are hard history with no community reader; unit 4 (forced labor) and unit 9 (war's human
  cost) have no read named at all.
- **Why it matters.** The reads are planned, and people sought, from this sentence.
- **Fix.** "Every unit gets the fresh-agent sensitivity read (bar item 12). A reader from the community concerned
  reads unit 2 (caste, including a Dalit reader), units 8 and 10 (slavery) and unit 6 (Aboriginal, Torres Strait
  Islander and Maori peoples)." Add the reads to the last column of units 2, 4, 8, 9 and 10.
- LAYER frame. REPEAT new (same kind as the grade 6 frame read of the same day). Confidence: firm.

### 3. Claim, evidence and reasoning first appears in unit 9, though claims are written from unit 1

- **What is wrong.** "Writing from sources" has short sourced claims in units 1 to 7, but Models carried lists
  claim-evidence-reasoning as "first used" in unit 9 (ss7-research-greek), and no unit 1 to 8 row carries the model.
- **Why it matters.** The lens's day check: "a claim is asked for with no model of claim, evidence and reasoning
  earlier in the unit". Writers of units 1 to 8 will not see the model they should hold, or the day it is
  withdrawn (C7).
- **Fix.** Models carried: "claim-evidence-reasoning | ss6-research-contribution, ss6-changing-interpretations |
  Unit 1 (ss7-indus-valley, a short claim about an object, with retrieval from grade 6) | Units 2 to 8 short claims;
  unit 9 (ss7-research-greek); unit 12 (with the opposing claim)". Add claim-evidence-reasoning to model_in of
  ss7-indus-valley.
- LAYER frame and progression. REPEAT new. Confidence: likely.

### 4. Unit 3's compelling question covers a third of the unit

- **What is wrong.** "Why did China's rulers claim heaven's approval, and what happened when they lost it?" fits
  the Mandate of Heaven; it leaves out East Asia's geography (four codes, MA.7.T2a.1 to T2a.3 and T2b.1) and
  Confucius and Taoism (T2b.2b).
- **Why it matters.** Bar item 1 fails a unit whose question is answered without its content.
- **Fix.** "What held early China together: its land, its rulers or its teachers?" (geography, the Mandate and
  dynastic cycle, and Confucian and Taoist ideas all answer it, and more than one answer can be defended).
- LAYER frame. REPEAT new (same kind as the grade 6 read). Confidence: likely.

### 5. The action in unit 8 has no held day to look back

- **What is wrong.** The action cycle takes "about 4 of the 15 days" of unit 8 and ends with a look-back, but a
  letter to the principal or a council proposal gets its answer weeks later. Grade 6 holds a look-back day about
  four weeks on; grade 7 does not.
- **Why it matters.** The look-back is the part of informed action that teaches what action does; done the same
  week, it looks back at nothing.
- **Fix.** Add to "Informed action": "One of unit 8's days is held for the look-back about four weeks later; the
  scope and sequence places it at the start of unit 10." Same sentence in ss7-athenian-democracy's notes.
- LAYER frame. REPEAT new. Confidence: likely.

### 6. Two seams live in prose but not in the data

- **What is wrong.** (a) ss7-rome-fall's notes say "answering a counterclaim in full comes in grade 8
  (ss8-haudenosaunee-influence ...)", and the grade 8 frame picks it up from ss7-rome-fall, but ss7-rome-fall's
  hands_on lists only wh1 rows, ss8-haudenosaunee-influence assumes nothing, and this frame's "Handed on" table
  omits it. (b) Grade 6 hands Christianity's place in the empire to "grade 7's Rome units ... as review"
  (ss6-christianity-origins); only unit 12's cell here says so, no ss7 row does.
- **Why it matters.** The gate and the reading packs follow the columns; a grade 8 writer will not get a readiness
  check on the opposing-claim move, and a unit 12 writer working from the row will not teach Christianity's rise in
  the late empire, which the "fall or transformation" debate needs.
- **Fix.** (a) Add ss8-haudenosaunee-influence to ss7-rome-fall's hands_on and ss7-rome-fall to its assumes; add a
  row to "Handed on": "Naming the strongest opposing claim | ss7-rome-fall | ss8-haudenosaunee-influence answers
  counterclaims in full". (b) Add to ss7-rome-fall's notes: "Christianity's growth in the late empire (Constantine,
  then a state religion) returns as review of ss6-christianity-origins, as evidence in the transformation debate."
- LAYER progression and frame. REPEAT new. Confidence: firm.

### 7. One cross-subject lean is missing from the table

- **What is wrong.** e7-reading-range (ELA 7, thread 1) reads beside ss7-athenian-democracy, ss7-roman-republic and
  ss7-greek-myth. The table lists only the Athenian lean (unit 8).
- **Why it matters.** The ELA 7 frame will not know the republic texts need unit 10 (days 121 to 133).
- **Fix.** In the e7-fiction-and-history line add "e7-reading-range's Rome and myth texts lean on ss7-greek-myth
  (unit 9, days 102 to 116) and ss7-roman-republic (unit 10, days 121 to 133): ELA 7 places them during or after
  those units".
- LAYER frame. REPEAT yes (cross-subject timing, progression-cross-2026-11-13). Confidence: firm.

### 8. Stale note: frames.csv

- **What is wrong.** "For the lead" 5: "Not edited here; `python -X utf8 scripts/frame.py sync` writes the row".
  The row is in data/plans/frames.csv (12, 160). Unmarked, so stale.py passed it.
- **Fix.** "frames.csv carries the row (12 units, 160 days), written by `scripts/frame.py sync`; rerun it if the
  unit count changes."
- LAYER process. REPEAT yes. Confidence: firm.

## The lens checklist (course frame layer)

| Line | Met, missed or not applicable |
|---|---|
| An anchor standard in the course's topic range has no unit | Met (gate; 58 of 58 counted by hand) |
| The replaced grade 3 year or "your state" keeps Massachusetts-only content | Not applicable |
| No unit lists what the check set adds, or an addition has no recorded source | Met: every unit has the column, each candidate names its source |
| Chronology across grades | Met: ends about 500 CE where grade 9 opens; the Japan and Oceania runs past 500 are named |
| History in time order, or a reason | Met: by region, in time order within each; the return to 1200 BCE at unit 8 follows the anchor's regional order |
| A contested question has more than one telling | Met: Indo-Aryan arrival as a scholarly question; Rome's fall as a historians' debate |
| Writing from sources builds short to long | Met (units 1 to 7, 9, 12), with finding 3 on the model |
| Sensitive topics and the reads | Missed in part (finding 2) |
| Informed action once a year, chosen by students | Met, with finding 5 on the look-back |

## What is right and should not be touched

- The Indus unit's move: inferring maker, date and audience for objects with no readable script (D2.His.11), built
  on grade 6's Kush.
- Caste told plainly and fairly, untouchability outlawed in 1950 and still an issue, no student asked about family
  caste or faith.
- The comparison that never ranks peoples, on parallel timelines with grade 6's traits.
- Supply and demand introduced on Silk Road prices and reused on Roman money; the 33 CE case marked for checking.
- Aboriginal, Torres Strait Islander and Maori peoples in the present tense with the image and sacred-site cautions.
- The counterclaim taught as a word and move here, answered in full in grade 8.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| The Han dynasty is taught in unit 4 as part of MA.7.T2b.2f, not as a check-set addition | 2f's Silk Road trade and Buddhism's arrival are Han events | frame unit 4, "Check set adds", "For the lead" 2; ss7-silk-road-trade notes |
| Technologies dated on the timeline: bronze (Shang, unit 3), silk, paper (Han), gunpowder (Tang, as a pointer past 500) | MA.7.T2b.2e taught without misdating | ss7-qin-unification notes; frame unit 4 |
| A short Persian Empire opener (Cyrus, Darius, its roads) inside unit 9's wars | MA.7.T4b.5 asks the causes of the Persian Wars, which cannot be taught without Persia; inside the unit's days | frame unit 9 "Check set adds" (moves from candidate to placed) |
| Unit 8's look-back day held to the start of unit 10 | About four weeks after the action, as grade 6 | frame "Informed action"; ss7-athenian-democracy notes |
| 45 minutes a lesson | Agree with the pick; C2 needs a stated length | scope and sequence |

## For Cory

- People: with finding 2, grade 7 needs readers from the community concerned for units 2 (including a Dalit
  reader), 6, 8 and 10, not unit 6 alone.

## What I could not judge

- No grade 7 ELA or math frame exists, so the time-zones, percent, research and argument leans are checked against
  the progression rows only.
- No World History I frame exists; the hand-on at about 500 CE is checked against the wh1 rows only.
  Since written (2026-11-13): the World History I frame's 'Picked up' table matches every grade 7 hand-on row for row
  (checked in frame-world-history-i-2026-11-13.md).
- C3 wording rests on memory (ids only in the repo). Finding 1's dates rest on memory of well-established
  chronology; the day writer should still source each date.

## Sources

- data/standards/ma-hss-2018.txt: MA.7 codes counted and traced (T2b.2e, T2b.2f, T4b.5 read for findings 1 and the
  settled Persia item).
- data/standards/c3-indicators.txt: C3 ids; wording from memory.
- docs/ADOPTION-BAR-SUBJECTS.md (C1, C3, C7, C12, section 1 items 1, 8, 12) and docs/FOUNDATION.md section 7.
- docs/agents/lenses/social-studies.md: the checklist above.
- No outside source was fetched this run; nothing new for the source list.

Defects were not logged with `scripts/plan.py defect`: the caller asked that only this report be written.
