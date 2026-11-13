# Expert cold read: math-4 unit 4 re-plan, days 29 to 38 (2026-11-13)

Job: docs/pipeline/briefs/plan-read.md, course math-4, unit 4, days 25 to 38. I am the curriculum expert (docs/agents/EXPERT.md), reading cold. I edited nothing; the lead saved this report. Agent run: 208,632 tokens, 29 tool uses.

## What I read

- `python -X utf8 scripts/plan.py check`: 810 items, 0 failures. Notes for this unit:
  - day 33 does not check "subtract mixed numbers two ways";
  - day 35 does not check "check my answer";
  - s04-X30 and X37b ask "why" but are keyed;
  - s04.md has 2,178 words of prose.
- `plan.py pack math-4 4` in full: s04.md and u04-1.md to u04-4.md.
- source-map.csv, handbacks.csv, materials.csv and reserved.csv, all in data/plans/math-4/, against data/plans/README.md ("Cross-day files and the source map").
- The days.csv rows for days 29 to 38, and the items.csv rows for K29 to K34, P33, X33 to X35, W34, F30 and F37.
- The openers in courses/math-4/u04-2 to u04-4, and u04-1/record.md.
- d028.md in full, and the print and material lines of d024 to d028.
- IM grade 4 unit 3, lessons 8 to 12: warm-ups, activities, syntheses and student tasks. Lesson 15 and the unit overview, to place lessons 15 to 20.
- Earlier reviews: plan-s04-2026-11-12, reliability-u04-d025-028, day-025 to day-028, and cheap-d025 to d028.

## Verdict

The re-plan is sound for learning. Mixed numbers now come after joining and separating, which fits 4.NF.B.3a before 3c, and each keep, split and cut in the source map holds against the IM lessons.

The biggest risk is day 33, the day that carries the standard's "two ways":
- its exit checks only adding;
- its minutes are thin for its main idea;
- its worked example and its three-answers task both land past the end of the printed line to 5.

The fixes that matter most: rebuild day 33's minutes and exit together (finding 1), and run section 4.3's line from 0 to 6 (finding 2).

Thirteen findings, none blocking. Eleven are about facts that cross days: sequence 3, hand-backs 2, materials 6, reserved examples 0.

## Findings, most serious first

### 1. Day 33's exit checks only adding, and the day's main idea is short of minutes

LAYER plan. REPEAT yes (plan-s04-2026-11-12, findings 3 and 4). Firm.

**What is wrong**
- The goal names subtracting both ways, and day 33 teaches 3 4/8 − 1 1/8 both ways, but E33 is one sum.
- E34 does not cover this: it checks subtraction that needs a broken whole.
- Teaching first has 12 minutes for four computations plus the side-by-side argument.
- The three-answers task gets 7 minutes, where IM gives it about 15.
- A light tool takes 15 minutes.

**Fix**
- E33 gains part (b): "4 7/12 − 2 3/12 = __. Check by adding."
  - Answer: 2 4/12 (or 28/12, or 2 1/3).
  - Wrong answers: 2 4/0 (A); 6 10/12 (x, added).
- Day 33's minutes:

  | Part | Minutes |
  |---|---|
  | Warm-up | 5 |
  | E32 back | 3 |
  | Teaching | 14 |
  | Tool | 10 |
  | By hand | 21 |
  | Exit | 7 |

- The handbacks.csv row for day 33 to day 34 adds (b).

### 2. Day 33's examples run past the end of the line to 5

LAYER plan. REPEAT new. Firm.

**What is wrong.** K33-1 (sum 5 2/5) and P33-1 (sum 5 4/8) both land past 5.

**Fix.** Section 4.3's printed line runs from 0 to 6 on days 32 to 34. Change "to 5" to "to 6" in:
- s04.md field 2;
- u04-3.md fields 5 and 11;
- the u04-3 opener;
- days.csv rows 32 to 34;
- Recipe Scaler ask 2.

### 3. Unit 4's record sheet is never printed, and its materials row hides that

LAYER process and plan. REPEAT yes. Firm.

**What is wrong**
- record.md covers days 24 to 39, and readiness items are recorded on it from day 24.
- d024 prints only unit 3's record sheet.
- Days 25 to 28 record on unit 4's sheet, but none of them prints it.
- The materials row (made day 25, used days 29 to 38) leaves out exactly the written days the gate would fail.

**Fix**
- d024's print line gains unit 4's record sheet.
- The materials row becomes made day 24, used days 24 to 38, with day 39 noted.
- d025 to d028 name the sheet in their materials lines, and so does every plan row for days 29 to 38.
- Do not narrow `used_days` to pass the gate.

### 4. Day 28's error A hand-back lands on the wrong form, and the "x" students have no slot

LAYER plan. REPEAT yes. Firm.

**What is wrong**
- Day 28 sends 3/0 or 7/0 (error A, bottoms taken away) to day 29's teaching, but day 29's wrong example A is 2/8 + 3/8 = 5/16 (bottoms added). Those students never see their own error.
- The 13/6 and 19/100 students have no time on day 29.
- Day 29 otherwise picks up day 28 exactly.

**Fix**
- After wrong example A, one minute on "2/8 + __ = 5/8 is not 3/0: what size are the parts?". By hand goes from 22 to 21 minutes.
- E28 back adds: "13/6 or 19/100: those students, at your table, read the blank aloud and check by joining."
- The handbacks row for the A hand-back is updated to match.

### 5. Three hand-backs call for strips or a line their day does not hold

LAYER plan. REPEAT yes. Firm.

**What is wrong**
- Day 35's E34 branch uses a broken strip, but day 35 is sketch only.
- Day 36's E35 branch uses a strip, but day 36 holds only the tape.
- Day 38's group G hops on a line, but day 38 prints none.

**Fix.** No new print:
- Day 35: the teacher breaks one whole strip under the camera, and students sketch it.
- Day 36: a sketched tape cut into tenths.
- Day 38: group G sketches a line from 5 to 7 in the item's part size.

### 6. Day 34: the break skips the step that gives its reason, and its teaching is short

LAYER plan. REPEAT new. Likely.

**What is wrong**
- K34-2 writes 5 1/4 = 4 + 1 + 1/4 = 4 + 5/4.
- IM lesson 11, Activity 2 has the step 1 = 8/8. That step ties back to b/b on day 27, and it is the reason the break works.
- Day 34's rows add up to 58 minutes.
- Day 34 is labelled Fluency, but it is first teaching.

**Fix**
- K34-2 and u04-3 field 1 become 5 1/4 = 4 + 1 + 1/4 = 4 + 4/4 + 1/4 = 4 + 5/4.
- Teaching first goes to 12 minutes.
- Day 34's kind becomes Understanding, so the balance becomes 8, 2, 3, 1, and the scope and sequence's balance row changes to match.

### 7. Day 29's warm-up, as adapted, cannot be answered

LAYER plan. REPEAT new. Firm.

**What is wrong.** A line with only 0 labelled has no scale.

**Fix.** Ticks in thirds from 0 to 2, with only 0 and 5/3 labelled: "What is one space? Where are 1 and 2?" This is IM's version.

### 8. Day 35's exit misses two goal pieces, and IM lesson 12's mixed-number half was lost

LAYER plan. REPEAT yes. Firm for the exit, likely for the rest.

**What is wrong**
- The goal names "choose a way" and "check my answer", and E35 asks for neither.
- IM lesson 12, Activity 1 ("make it true" with mixed numbers, the unknown in any place) is lost. Day 28 used only its fraction half.
- Day 35's sort uses differences only; IM's mixes in sums.

**Fix**
- E35 (a) adds "Check by adding."
- E35 (b) adds "Circle the way you used: as fractions, or wholes and parts."
- The exit takes 6 minutes, and the keyed set goes to 11.
- The keyed set gains two items: __ + 1 6/10 = 5 3/10 (answer 3 7/10) and 6 − 2 11/12 = __ (answer 3 1/12).
- Two of the eight sort cards become sums: one with parts past a whole, one without.

### 9. Day 30's short strip is sound, but day 37 needs one more fold

LAYER plan. REPEAT new. Likely.

**What holds.** Fold the strip in half and cut on the fold, and the length is exact. Blank strips used: 6 of 10. One fourth of the short strip equals one eighth of the long strip, which is harmless if the talk stays on "fourths of what?".

**What is wrong.** Day 37's example is in eighths, but both strips are folded in fourths.

**Fix**
- On day 37, fold both strips once more into eighths (1 minute).
- On day 30, keep the spare half in the envelope.

### 10. Day 36's goal claims day 37's content

LAYER plan. REPEAT yes (stale plan text). Firm.

**Fix.** The goal becomes: "I can solve a story with mixed numbers when the change is unknown or two amounts are compared, using a tape and an equation."

### 11. The facts group misses the warm-ups that launch days 29 and 30

LAYER plan. REPEAT new. Judgment call.

**Fix.** On days 29 and 30 the facts group joins the warm-up and does its facts on the take-home sheet.

### 12. Source map: one row is incomplete, lessons are unaccounted for, and a claim is wrong

LAYER process. REPEAT new. Firm.

**What is wrong**
- The lesson 9 row for day 30 omits Activity 2.
- "Last item moves to day 34" understates the change: four of six items move.
- Lessons 15 to 18 and 20 have no row.

**Fix**
- Lesson 9: Activity 2, items 1 to 3 on day 30; the items from 1 5/8 on day 34.
- Add rows:
  - lesson 15, cut (unlike denominators);
  - lessons 16 to 18, unit 7;
  - lesson 20, cut (optional).

**What holds.** The rest of the map is sound for learning.

### 13. s04.md is over its prose cap: 2,178 words against 1,250

LAYER plan. REPEAT yes. Firm.

Cut about 950 words of restated files and history:

| Part | Cut |
|---|---|
| Header | about 100 |
| Field 2 | about 80 |
| Field 5 notes | about 220 (reserved list to one sentence; drop the E37 collision history) |
| Field 6 | about 30 |
| Field 7 | about 40 |
| Field 8 | about 300 (keep the tool verdict and a pointer to materials.csv) |
| Field 10 | about 180 (keep IES pages, "Carried to unit 5", "Not sourced", and "Balance: 8, 2, 3, 1") |

## Settled by the expert

Every fix above, plus:
- The keys for E30 (b) and E37 (b) hold yes or no. The "why" is read by the teacher with one look-for: "names two different wholes".
- Days 36 and 37 stay ours. IM has no lesson with a tape or a start unknown, and they are the test's control days.

## For Cory

Nothing. Every choice stays inside 4.NF.B.3 and inside unit 4.

## What is right and should not be touched

- **The order:**
  - add (29)
  - subtract (30)
  - stories under 1 (31)
  - mixed numbers (32 to 35)
  - stories with the unknown anywhere (36 to 37)
- **Day 33's three right answers**, and the rule that a sum not yet renamed gets a tick plus group G.
- **Hand-backs.** Every exit from 29 to 36 has 3 minutes and one action. Written tasks come back the next day, E37 is read the night before day 38, and 4.1c is carried to day 39. This fixes the main cross-day failure of days 25 to 28.
- **Reserved examples:** no collision.
- **Day 34** uses lesson 11's one-line layout, and places lesson 10's whole minus a fraction first.

## What I could not judge

- Whether 6 minutes on day 30 is enough to cut, fold and talk.
- Whether the envelope holds enough fourth-pieces for day 32's 13/4.
- Days 36 and 37 are Application days, while the adapted days are mostly Understanding, so the control differs in kind as well as in source.

## Count of findings that cross days

| Kind | Count |
|---|---|
| Sequence | 3 |
| Hand-backs | 2 |
| Materials | 6 |
| Reserved examples | 0 |
| **Total** | **11 of 13** (two of the eleven are in written days: d024's record sheet and d028's A promise) |

## Sources

IM K-12 Math grade 4 unit 3, lessons 8 to 12 and 15, plus the unit overview (CC BY 4.0, local copies). Progressions NF 3 to 5, PDF pages 150 to 153, as cited earlier (not reopened). No new source.
