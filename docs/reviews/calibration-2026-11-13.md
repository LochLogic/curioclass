# Calibration run 1: the expert reader (P5d), 2026-11-13

The first run of docs/pipeline/CALIBRATION.md. Six fresh expert agents, one per piece, each read cold with its
normal brief (progression-read, frame-read, plan-read) and the subject lens, and returned a report. Scored by the
lead against `S:\CurioClass-sources\_calibration\key\faults.csv`, with `key\correct\` used to tell planted faults
from findings on the draft as built. **Codex's half is pending:** Cory pastes the six prompts in
`_calibration\prompts\CODEX-PASTE.md`, each into a new chat.

## Result against the line

| Line | Expert | Met? |
|---|---|---|
| Catch at least 15 of the 18 planted majors | **18 of 18** (one, P10, caught but ranked minor) | Yes |
| At most 3 false major alarms | **4 raw; 1 after the test's own fault is taken out** (see below) | Yes, on the corrected count |
| The 4 rejected past findings judged false at least 3 times in 4 | **4 of 4** | Yes |
| No fault kind missed in all its plantings | Every kind caught every time | Yes |
| Top finding is a planted major in at least 3 of the 4 pieces | Progression (math) yes, unit plan yes, science yes; frame no (its top finding was the planted minor, a day count) | Yes, 3 of 4 |

**Verdict: the expert reader passes for progressions, frames, scopes and sequences and units**, with two notes
below (severity of count errors, and leniency on real past findings). Its reads can be trusted alone once Codex's
half is scored; if Codex falls under the line, Codex is not used alone for that layer, and the expert's pass stands.

## Caught and missed, by piece

| Piece | Planted majors | Caught | Minor caught | Unplanted majors raised |
|---|---|---|---|---|
| Math progression | P1, P2, P3 | 3 (findings 1, 2, 3) | M1 (finding 8) | 1, real: nf5-multiply's notes drop 5.NF.B.5b's "why" and 5.NF.B.6's mixed numbers |
| Social studies progression | P4, P5, P6 | 3 (findings 6, 8, 4) | (none planted) | 4: three false (below), one real (conquest left out of MA.4.T3) |
| Grade 5 frame | P7, P8, P9 | 3 (findings 3, 2, 6) | M2, but ranked first and marked major | 4, real: the check after unit 2 asks for a two-source claim before unit 3 teaches it; a year-end counterclaim no unit teaches and above the C3 3 to 5 band; MA.5.T2.1c's first battles fall between units 3 and 4; unit 7's question (follows from P8) |
| Math unit plan | P10 to P14 | 5 (findings 1, 2, 3, 4; P10 in finding 9, as minor) | M3 (finding 7) | 1, judged false (below) |
| Science unit | P15 to P18 | 4 (findings 5, 1, 4, 2) | M4, marked major | 1, real: MS-PS1-1 (molecules and extended structures) taught in lesson 9 but never assessed |

By kind: owned-twice 3 of 3, handoff-skip 3 of 3, model-before-taught 4 of 4, standard-in-part 3 of 3,
values-miss 2 of 2, exit-misses-goal 3 of 3.

## False major alarms

1. to 3. **Social studies progression, findings 1 to 3** (grade 4 regions missing, grade 5 topics 4 and 5
   missing, ss5-republic-growth "does not exist"). The slice is an excerpt (grade 4 history and grade 5 topics 1 to
   3), and set\README.md says so, but the prompt barred the reader from everything under `_calibration` except the
   draft, so the reader could not see the scope. These are the test's fault, not the reader's. The math reader,
   given the same bar, marked out-of-slice ids "could not check" instead. **Fixed for Codex and later runs:** every
   piece prompt now allows set\README.md.
4. **Math unit plan, finding 5** (mixed-number notation used from day 27, before section 4.3). The line is s04.md as
   held after its own expert read; the base text brings in wholes plus a fraction at the same point, and the
   reader says the order is defensible. Stating it in the carried list is a fair minor; as a major it is a false
   alarm.

## Past findings (claims)

| Claim | Truth | Expert | Note |
|---|---|---|---|
| 1 | true | false | Judgment: the reader held that "whole floor" and "along all four edges" still leave the choice to the student. The original fix said they give it away. Lenient. |
| 2 | false | false | |
| 3 | true | true | |
| 4 | false | false | |
| 5 | true | true | |
| 6 | false | false | |
| 7 | true | false | **The excerpt was faulty**: it shows the key (8 4/5; 7 9/5) but not the answer the key marked wrong, so the claim could not be judged true from it. Test fault. |
| 8 | true | true | |
| 9 | false | false | |
| 10 | true | false | Judgment: the reader held a reteach set of composites still breaks error F. The original fix added a prime so the search can end in "finds nothing". Lenient. |

Rejected findings: 4 of 4 judged false (the line). Real findings: 3 of 6 judged true, 4 of 5 counting only fair
excerpts. Not part of the line, but it shows a lean: **the expert gives a draft the benefit of the doubt on
judgment calls** about whether an exit or reteach set does its job. A cold read that leans lenient misses faults;
the planted set did not show it because plantings are clean.

## What to change

- **Test (done):** prompts allow set\README.md. Next set: claims excerpts checked for being judgeable on their own.
- **Severity of counts (the prompt's major/minor line, next set):** a day total that does not add up was marked
  major twice and led one report. Major and minor are defined only in the calibration prompt (no brief uses them),
  so the rule goes there: a count mismatch is minor unless the right number cannot be told from the draft. Codex's
  run keeps the expert's prompt unchanged so the two compare.
- **Leniency (watch, no change yet):** two real past findings judged false on judgment. If Codex shows the same, add
  to EXPERT.md: "when an exit or a set could be read as doing its job or not, say which reading a tired writer
  takes".
- **Scope of the read:** the social studies reader opened docs/courses/social-studies/STANDARD.md and the grade 3
  outline (barred by the prompt's "nothing under docs/courses"); neither is a copy of the draft, so the result
  stands. Next run names those two as allowed.

## Unplanted findings worth carrying into real work

- MA.5.T2.1c's named events, unit 7's crowding (11 standard lines in 24 days), and the year-end counterclaim
  above the C3 band: the real grade 5 frame should be checked for all three when it is written.
- Science: assess MS-PS1-1's extended structures in any unit that teaches them; candidate gases in a "sinks in air"
  test cannot include nitrogen.
- Social studies: MA.4.T3's conquest must reach the notes, with a teacher note.

## Codex half

Pending. Prompts: `S:\CurioClass-sources\_calibration\prompts\CODEX-PASTE.md` (six, one per new chat). Each
writes to `_calibration\returns\codex-<piece>.md`. Codex reads with the README fix in place, so its false-alarm
count is not comparable one to one with the expert's raw 4; compare with the corrected 1.
