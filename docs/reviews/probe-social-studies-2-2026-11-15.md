# Probe report: social studies, second section (2026-11-15)

The second probe under docs/pipeline/PROBE-GUARD.md, written from the corrected social studies unit plans. One
section of World History I (unit 3, section 3.4, days 42 to 46: mapping Mali, the Swahili coast or the Mongol Empire
and defending a claim) was written by Codex and read the full way: cheap read, five expert reads, sensitivity read,
fix pass, fresh re-read, closing pass. The first probe is docs/reviews/probe-social-studies-2026-11-15.md.

## Result: Off on all three measures. The fault has moved, though.

| Measure | Reading | Band | First probe |
|---|---|---|---|
| 1. Plan share | 88 of 147 findings (60%) have origin unit, scope, frame or template | **Off** (over 35%) | 60%, Off |
| 2. Unit plans changed | 57 of 137 other units (42%) need a fix of the same kind; 33 (24%) without F5 | **Off** (over 25%) | 88%, Off |
| 3. Template or one unit | Rule lines and gates, plus one new required table in UNIT-PLAN field 7 (social studies) | **Off** on a strict reading | On |

No finding had origin frame.

## Measure 1: plan share

Source: data/plans/defects.csv, course world-history-i, dated 2026-11-15, rejected rows left out (3), and the
re-read's five reopened rows not counted twice. MEASURED.

| Origin | Findings |
|---|---|
| unit | 75 |
| template | 12 |
| scope | 1 |
| frame | 0 |
| section | 37 |
| day | 22 |
| **All** | **147** |

Plan share = (75 + 12 + 1) / 147 = 60%. Expert findings alone: 39 of 65 (60%; first probe 63%).

**Where the unit-origin findings sit.** Only 6 needed the unit plan itself (s03.md). The rest are the unit's
cross-day data made when the plan is turned into data (plan-data.md step 2 and 3): answer keys, samples and
look-fors in items.csv (22, kind key), source sheets and sources.csv (17, kind source), coverage (9), materials (5).
In the first probe sources led (21) and keys were 10; the error register fell from 7 to 4 after the letter rule.
So the unit plans Codex wrote now hold up much better; the step that writes keys, samples and source sheets from them
does not.

## Measure 2: unit plans changed

Full read in docs/reviews/probe2-measure2-2026-11-15.md, the faults found in s03.md checked across the 137 other
social studies units (one read for the same fault).

| Fault | Units |
|---|---|
| F1: feedback and revision inside the period the work is made, then scored (K2 kind) | 21 |
| F2: a wrong answer under a letter that does not describe it (K7) | 5 |
| F3: one wrong answer tagged with two letters, "D or I" (K1) | 12 |
| F4: a planned quotation with no free checkable translation | 3 |
| F5: an end item built on our own summary of a source, or one not read | 34 (least sure; about 20 on a narrow reading) |
| **Any of F1 to F5** | **57 of 137 (42%)**; 33 (24%) without F5 |

F6 apart: no unit has the component-to-move table field 7 now asks for (a rule added in this probe).

F1 and F3 are the kinds the first correction pass was sent to fix. They survived it in about a quarter of the units:
the pass was told the rule, and a gate caught only the semicolon form.

## Measure 3: template changes

From docs/reviews/fix-u03-4-2026-11-15.md. Small: `sensitivity` as a reader in plan.py; the teacher-prose cap per
minute of the course's day (an existing rule now gated, which trimmed US History I day 79 to 748 words); assessment
days that score earlier work take the teaching cap; a reserved-source gate; `endlooks` on the record sheet; a check
line that a judged exit is not its worked example; social studies rule lines in LESSON-DAY (fresh stimulus, parallel
case on respond days, scale as a label, "Scored from the work you handed in", a key per rotated form, glosses only
for words used). One is shape: UNIT-PLAN field 7 now asks social studies units for a component-to-move table that
forms the respond day's groups. That is a required table added, so Off on the guard's wording, though it adds and
removes nothing else.

## The re-read and closing pass

docs/reviews/reread-u03-4-2026-11-15.md: of 130 fixes, 125 hold, 4 in part, 1 not; 11 new findings (unit 8,
section 3). The most serious: a read-aloud rule put "the people of Mali" in place of "Tartars", and a free English
Secret History of the Mongols exists (CEDAR 2015, CC BY-NC-ND) that the sheets said did not. The closing pass fixed
these (fix-u03-4 report, "Closing pass"); a short word-for-word excerpt of the Secret History is now quoted with
credit, as the licence allows for a free, non-commercial site.

## Back to the builders

Do the lessons reach the next writer? Expert readers tag each finding as a repeat of a kind already seen or new.

| Probe | Expert findings | Repeats | Share |
|---|---|---|---|
| First (US History I 5.2) | 54 | 26 | 48% |
| Second (World History I 3.4) | 65 | 38 | 58% |

Repeats rose. Part of that is more history to match against, but the measure 2 read shows the same thing directly:
F1 and F3 were in the correction brief and survived. Rule lines in briefs are not enough for Codex; gates are. Where
each repeated kind goes now:

| Kind | Goes to |
|---|---|
| Two letters on one wrong answer, any form ("D or I", "(B, G)") | Gate: unitplan.py fails it |
| Feedback and revision inside the period the work is made, then scored | Gate where the data shows it (handbacks.csv: a scored part needs a hand-back row from an earlier day); rule line in the plan-codex briefs |
| Keys, samples and look-fors that pass a wrong answer or say more than the sheet | Process: an answer-key read (sensitivity-read.md kind `answer-key`, solve cold first) after plan-data and before days are written |
| Source sheets with unchecked or summary text | Gate exists (placeholders fail); add: every sheet passage has a sources.csv row with a link and a checked status |
| Reserved source named early, caps, exits that redo the worked example | Gates and check lines added in this probe |
| Component-to-move table (F6) | Rule in UNIT-PLAN field 7 and the plan-codex briefs; unitplan.py notes a missing table |

The repeat share is tracked for every probe from now on: if it does not fall, the builders are not learning.

## What happens next

The guard's table says: correct the units, then probe once more before the next subject. The call for Cory is
whether science, ELA and math units wait for that third probe (Desk card q-probe-ss-2):

1. **Gates first** (the table above), then a second Codex correction pass of the social studies units, run to the
   gates rather than to the brief.
2. **Science, ELA and math units** written with the same gates and rules from the start.
3. **A third social studies probe**, in a third course, read the same full way, with the answer-key read added after
   plan-data.

The pick: run 2 and 3 side by side (Codex Pro ends 2026-11-30, and 259 units are the largest Codex job left), rather
than 2 after 3. What argues for it: only 6 of 147 findings needed a unit plan; the faults left in the unit plans are
the gateable kinds; the weak step, plan-data, runs at day time for every subject anyway, after the guard. What argues
against: if the third probe changes the template's shape again, three subjects' units take a second pass.
