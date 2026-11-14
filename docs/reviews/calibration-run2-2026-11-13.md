# Calibration run 2: both readers, fresh plantings, 2026-11-13

The re-run docs/pipeline/CALIBRATION.md asks for after EXPERT.md gained two rules in run 1 (read an exit or set the
way a busy writer and a student would; severity follows the cost to a writer, so a count slip is minor unless the
right number cannot be told). later.csv L10. Same five base pieces as run 1, fresh plantings (18 majors, P1 to P18,
and 4 minors, M1 to M4, one new kind: a count whose right number cannot be told), and 10 claims re-cut so each
excerpt can be judged alone. Prompts allowed set\README.md, STANDARD.md and the grade 3 outline. Six fresh expert
agents and six Codex runs (by script, no pasting), each piece read cold. Set, key and returns in
`S:\CurioClass-sources\_calibration\run2\`.

## Result against the line

| Line | Expert | Codex | Met? |
|---|---|---|---|
| Catch at least 15 of the 18 planted majors | **16 found** (P10, P17 missed); 15 rated major (P18 rated minor) | **17 found** (P16 missed); 16 rated major (P18 rated minor) | Yes, both |
| At most 3 false major alarms | **0**: its unplanted majors are all real base faults (in key\correct too) | **0 clear, 3 arguable** (below) | Yes, both |
| Rejected claims judged false at least 3 of 4 | **4 of 4** | **4 of 4** | Yes, both |
| No fault kind missed by both in all its plantings | Every planting caught by at least one reader | | Yes |
| Top finding a planted major in most pieces | **5 of 5** | **3 of 5**; the other two led with real base faults run 1 already judged real (the unit plan's "one sandwich" correction, the sealed-bottle pressure hazard) | Expert yes; Codex yes in substance, as in run 1 |

**Verdict: both readers pass again, and the two run 1 rules worked.**

## Did the EXPERT.md rules move the scores?

- **Leniency rule: yes.** Real past findings judged true: expert 5 of 6 (run 1: 3 of 6), Codex 6 of 6 (run 1:
  2 of 6). The expert's one miss was claim 5. Rejected findings stayed at 4 of 4 for both, so the stricter reading did
  not tip into accepting false findings.
- **Severity rule: yes.** Every recoverable count slip (M1, M2) was rated minor by both readers; in run 1 two count
  slips were marked major and one led a report. Both typos (M3, M4) minor.
- **One over-correction to watch:** P18 (unit header 21 days, lessons add to 23, lesson 7 and the section 2 heading
  agreeing with 23) was planted as a count whose right number cannot be told, so major. Both readers rated it minor,
  and Codex said the 23 is "recoverable from two consistent sets of allocations". The builder flagged P18 as
  arguable when it was planted. No change now; if a real draft shows the same pattern, add to EXPERT.md: "two totals
  that each add up but disagree, with no way to tell which was meant, is major".

## Caught and missed, by piece

| Piece | Planted | Expert | Codex |
|---|---|---|---|
| Math progression | P1, P2, P3; M1 | all, M1 minor | all, M1 minor; 2 unplanted majors (equivalence in one direction only, against BASELINE rule 23: real; student explanations not secured in three rows: arguable) |
| Social studies progression | P4, P5, P6; M3 | all, M3 minor | all, M3 minor; 3 unplanted majors (ss5-slavery-colonies "legal in every colony through the 1700s", Georgia barred it until 1751: real; claimed C3 indicators thinner than their directions, and three MA standards losing a part in the notes: arguable, a stricter depth reading than the base) |
| Grade 5 frame | P7, P8, P9; M4 | all, M4 minor | all, M4 minor; 1 more minor |
| Math unit plan | P10 to P14; M2 | **P10 missed**; others caught; M2 minor; unplanted: register row C "day 29: 6/10" (real) | all five; M2 minor; 3 unplanted majors (error E's "one sandwich" correction, found in run 1 too: real; E33(b) asks one subtraction method where part (f) promises two: real; 4.4a with no model and 4.2b keyed on the circle: real) |
| Science unit | P15 to P18 | P15, P16; **P17 missed**; P18 minor; unplanted: lesson 6 reading gives lessons 7 and 8 away, lesson 3 "how it melts", lesson 4 calls the gas a new substance before lesson 5 (all real) | P15, P17; **P16 missed**; P18 minor; unplanted: sealed-bottle pressure hazard, lesson 2 crossing out trapped gas on weak evidence, extended structures never developed (all three found in run 1 too: real), lesson 4's new substance (real, the expert's too) |

By kind, across both readers: owned-twice 3 of 3, handoff-skip 2 of 2, model-before-taught 3 of 3,
standard-in-part 4 of 4, values-miss 2 of 2, exit-misses-goal 3 of 3, count-untellable 1 of 1 found (both minor).
No planting was missed by both: P10 and P17 (expert misses) were caught by Codex, P16 (Codex's miss) by the expert.

## What follows

- **Both readers can read alone for every layer, as after run 1;** together on progressions and frames, where they
  still catch different things. Each missed a planted major the other caught, so a single reader at the baselines
  would have passed one in about 18.
- **The base pieces carry real majors that two runs have now found** (the unit plan's "one sandwich" correction, the
  sealed-bottle hazard, lesson 2's trapped-gas inference, the unassessed extended structures). They are calibration
  copies, not live work, but the same faults will be built again if the unit plan and science unit are written from
  the same base text. Carried into real work: the math grade 4 unit 4 plan and the middle school matter unit, when
  written, are checked for these.
- **No change to EXPERT.md, a brief or the lens from this run,** so no new calibration row is due. The next run comes
  at the next change to one of those, per CALIBRATION.md.
- Codex ran by script (scripts/codex_read.py) with no pasting; its run logs stay beside the returns, outside the
  repository.
