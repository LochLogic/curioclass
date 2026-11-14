# Sequence read: economics (Economics, with personal finance, half year), 2026-11-14

Expert cold read per docs/pipeline/briefs/sequence-read.md. Independent of any other read of this scope and sequence.

## What I read

AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/social-studies.md; the social studies part and part 8 (personal
finance) of docs/ADOPTION-BAR-SUBJECTS.md; docs/courses/social-studies/STANDARD.md; docs/courses/economics/frame.md;
docs/courses/economics/scope-and-sequence.md; data/plans/economics/days.csv (all 80 rows); the econ-* rows and
ss8-public-budget in data/progressions/social-studies.csv; MA.ECON and MA.PFL lines of data/standards/ma-hss-2018.txt;
docs/courses/CALENDAR.md and the grade 12 rows of data/plans/calendar.csv (ELA 12, US History II, US Government);
the Algebra II frame's lean row; the ELA 12 frame's writing calendar; docs/pipeline/briefs/sequence-write.md (rule 2);
docs/GLOSSARY.md (readiness check, retrieval task); the earlier frame read docs/reviews/frame-economics-2026-11-13.md.

Gates: `scripts/sequence.py` via `plan.py check`: economics 0 failures. `plan.py check` as a whole exits 1 on one
stale note in docs/courses/us-history-ii/frame.md (not this course). `frame.py calendar`: no stagger break; grades 9 to
12 have no rule outside the finals week, and the final check sits in week 32. `stale.py check`: no economics failure.

## Verdict

A sound half year: the anchor's order is kept, every ECON and PFL code and every owned C3 indicator is carried by a
named day, both new macro models and the market graph are kept apart, and every end-of-unit assessment has an unseen
task. The biggest risk is load in unit 9 (19 codes, three of them "create" or "research" tasks, in 8 coded teaching
days), with a lesser crush on day 28 and day 46; the frame's four readiness checks on the same grade 8 row spend time
that unit 9 and unit 4 need. The one change that matters most: open units 4, 8 and 9 with retrieval tasks rather than
second, third and fourth readiness checks on ss8-public-budget, and use the freed time and the paying-for-college day
to split day 73.

## Findings, most serious first

### 1. Unit 9 days far under its load (moderate; likely). LAYER sequence. REPEAT new

**What is wrong.** Unit 9 owns 19 codes in 11 days: 8 coded teaching days, the paying-for-college addition (day 72),
the assessment and the respond day. That is 2.4 codes per teaching day; units 1 to 8 run 1.0 to 1.75. Day 73 alone
carries ECON.T2.11, PFL.T3.7, T3.8, T3.9 and ECON.T6.6 (financial markets, what an asset is, how prices and returns are
set, diversification, and researching asset types from a source pack). Day 69 carries T2.3 (real and nominal), T2.4
(research saving policies and judge them) and ECON.T6.5 (a comparison matrix with a justified choice), plus a reteach
station. Two "research" verbs (T2.4, T6.6) get a fraction of a 50-minute period each.

**Why it matters.** C1 reads a code taught below its wording as untaught; "research" in one third of a period is
reading a summary. A unit writer will either cut the research or spill into the final check (day 79).

**Fix (days.csv rows 69, 71 to 73, 76; scope-and-sequence.md unit 9).** Inside unit 9's 11 days, no added day:
(a) Paying for college rides inside the credit plan (day 71: a student loan is one of the made-up offers compared) and
the savings plan (day 76: college offered as one goal), so day 72 is freed. The addition stays kept, at 0 added days;
the "2 of 4" count in the scope and sequence becomes "1 of 4". (b) Day 72 becomes financial markets and assets:
ECON.T2.11, PFL.T3.7, T3.8. (c) Day 73 becomes diversification and the asset-type research: PFL.T3.9, ECON.T6.6. With
finding 2, day 68 gains the time a readiness check took; move T2.3 (real and nominal rates) to day 68, leaving day 69 for
T2.4 and T6.5. Confidence: likely (load reasoning; the CEE 2010 standards and NSPFE 2021 treat investing and credit as
separate multi-lesson strands, from memory).

### 2. Four readiness checks on one grade 8 row in one half year (moderate; judgment call). LAYER frame. REPEAT new

**What is wrong.** Days 1, 28, 59 and 68 each open with a readiness check on ss8-public-budget, each with a reteach
station. Day 1 already checks "grade 8's opportunity cost, budgets and interest", the whole row. By week 22 the row is
not idle: the course checked it in week 17 and has used opportunity cost and budgets in every unit since.

**Why it matters.** Rule 2 of sequence-write asks for a readiness check where a unit "assumes an earlier grade's row
idle two or more grades"; GLOSSARY defines a readiness check as given before a unit on what it builds on from an
earlier grade. Once unit 1 has checked the row, what units 4, 8 and 9 need is a short look back, which is a retrieval
task. Each extra check costs 10 to 15 minutes in units already short (finding 1, finding 3).

**The right call for this course (the readiness versus retrieval question).** Unit 1: readiness check, as written.
Units 4, 8 and 9: retrieval tasks inside day 1 of the unit, on the part of the row each uses (public budgets, budgets,
interest); the unit 1 results name who joins the reteach station on days 29, 59 and 69. Unit 6: retrieval task, not a
readiness check (finding 4). Wh2 rows (grade 10, the year before for a grade 11 student and two years for grade 12)
open as retrieval tasks, as written; that is right for a course open to grade 11 or 12.

**Fix.** Frame, course in brief: "the one-lesson reteach of ss8-public-budget where it is dormant: units 1, 4, 8 and 9"
becomes "a readiness check on ss8-public-budget in unit 1 only, covering the whole row; units 4, 8 and 9 open with a
retrieval task on the part they use, and unit 1's results set who joins their reteach station". days.csv rows 28, 59,
68: `assess` blank, goal and note changed from "Readiness check" to "Retrieval task". Scope-and-sequence units 4, 8, 9
"Readiness" lines changed to match.

### 3. Day 28 and day 46 each hold two days of teaching (moderate; likely). LAYER sequence. REPEAT new

**What is wrong.** Day 28: a readiness check, a Depression retrieval task, public goods (T4.1), market failure, and
externalities drawn on the supply and demand graph (the check-set addition). Day 46: banks and other institutions
(T6.3), money creation through lending (an addition), the Federal Reserve's organization (T6.4) and the national bank
fight retaught. Each is a full lesson of material plus a second.

**Why it matters.** Externalities on the graph and money creation through lending are the two additions most likely to
be squeezed out, and both are what later days need (day 30's cost-benefit judgment; day 48's Fed tools).

**Fix (days.csv rows 28, 30, 45, 46).** Day 28: drop the Depression retrieval (it is retrieved again on days 37 and
47), keep T4.1 and market failure; move "externalities on the supply and demand graph" to day 30, where it is the
worked case for judging a policy's costs and benefits (T4.6). Day 45: with finding 4 freeing the readiness time, add
T6.3's "banks and other financial institutions" after the money supply. Day 46 keeps money creation, the Fed's
organization and the bank fight. Codes move with the content (MA.ECON.T6.3 onto day 45).

### 4. Unit 6's readiness check on grade 7 Rome checks nothing the unit assumes (minor; likely). LAYER sequence. REPEAT new

**What is wrong.** Day 45 is marked `readiness` on ss7-roman-economy, "with no reteach lesson, as the day teaches the
functions of money in full". "For the lead" 1 asks the frame to adopt this.

**Why it matters.** A readiness check whose result changes nothing is a check without a purpose; the day teaches T6.1
from the start, so the unit does not assume the grade 7 row. Debasement is a good hook for "store of value", which is
what a retrieval task is for.

**Fix.** days.csv row 45: `assess` blank; goal "Retrieval task on Rome's money and debasement (grade 7) as the hook;
then the functions of money and what counts in the money supply". Reject "For the lead" 1; instead the frame's seam row
for ss7-roman-economy reads "Unit 6, econ-money-banking: retrieval task (the day teaches money from its functions)".

### 5. D2.Eco.10's money supply is assessed before it is taught (minor; likely). LAYER sequence. REPEAT new

**What is wrong.** D2.Eco.10.9-12 asks students to use current data to explain how changes in spending, production
and the money supply affect the economy (C3, 2013, from memory of the wording; the progression row lists "money supply"
in its words). It sits on day 42 and is assessed on day 43, three days before the money supply is defined (day 45). Day
42's bridge (telling money for payments apart from income) does not teach the money supply's influence.

**Fix (days.csv rows 43, 49, 50).** Day 43's note: "checks D2.Eco.10's spending and production parts; its money supply
part is checked on day 50". Add D2.Eco.10.9-12 to the codes of day 49 (the policy day, where the money supply's
effect is the monetary lever) and day 50. Ownership stays with unit 5; no standard moves.

### 6. The portfolio is "tracked" across four consecutive school days (minor; likely). LAYER sequence. REPEAT new

**What is wrong.** The made-up portfolio is chosen on day 74 and observed on days 74 to 77 (school days 154 to 157).
ECON.T6.6 asks students to track investments, and PFL.T3.7 asks why asset values rise and fall over time. Four days of
made-up prices show noise, not the trade of risk and return over years.

**Fix.** Settled by the expert (table below): the dated observations are dated across years, from a printed made-up
price series built on published long-run returns of broad asset classes (stocks, bonds, cash), not across four school
days. The days stay where they are.

### 7. No long argument from sources in the half year (minor; judgment call). LAYER sequence. REPEAT new

**What is wrong.** The frame claims WHST.11-12.10 "routine short and long writing". The arguments (day 16, day 30,
day 49, day 75) are each one period. The claim-evidence-reasoning model is "named only in unit 9" (day 75) although
claims are asked from day 16.

**Why it matters.** Lens: writing from sources should build from short to long. Day 49 answers the unit 6 compelling
question, Congress or the Fed, which is the course's best argument prompt.

**Fix.** days.csv row 16 note: "Model: claim-evidence-reasoning retrieved (taught from kindergarten), with a counterclaim".
Row 49 goal: "a written argument of about a page from the supplied cases, with the other side's claim answered", and
the unit plan scores it on the course rubric. No day added.

### 8. Stale or loose lines (minor; firm). LAYER sequence. REPEAT yes (stale notes appear in most earlier reads)

- Scope and sequence unit 5: "Both new models open on the first two days". The aggregate graph opens on day 39, the
  third. Change to "the circular flow opens on day 37 and the aggregate graph on day 39".
- days.csv row 1 note says ss8-public-budget "skips 2 or 3 grades"; row 45 calls grade 7 "idle four grades or more".
  Grade 7 to grade 11 is three grades between; write "idle three or four grades".
- "For the lead" 2 cites the ELA 12 milestone days 135, 145, 147, 150 to 156 and 158. They are sourced: the shared
  research brief in docs/courses/us-history-ii/frame.md (unit 8 row) sets them. Accept "For the lead" 2 as written.
  The busiest overlap is school days 145 to 147 (ELA draft and rehearsal, US History II drafting); the US History II
  read (docs/reviews/sequence-us-history-ii-2026-11-14.md) handles it on that side, and nothing in Economics needs
  to move.

## Checked and found right (do not undo)

- Standards in full: every MA.ECON T1.1 to T7.8 and MA.PFL T1.1 to T4.2 code is on a teaching day and in its unit's
  end-of-unit assessment; every owned D2.Eco indicator and D2.Geo.11 is on a day.
- Order inside units: equilibrium, shifts, then controls; costs before marginal revenue; real rates after unit 5's
  inflation; comparative advantage made-up first, then real data. Nothing else used before taught.
- Two graphs kept apart (days 10 and 39), as the frame asks.
- Values: both lines of evidence on the minimum wage (day 16), trade's winners and losers (day 54), tax fairness (day 32),
  policy debates (day 49).
- Personal finance rules: made-up offers and brands, given figures, no family money asked; the six NSPFE areas placed.
- Informed action (days 62 to 63) after the consumer protection day it draws on, student-chosen, printed, with the look
  back on day 80.
- Lean A-SSE.B.4: Algebra II unit 2 runs weeks 3 to 9, so a grade 11 student has it before day 71; the payment-table
  bridge covers the rest.
- Calendar: check 1 on school day 115 (week 23), final on 159 (week 32, the finals week). No held look-back day shifts a
  unit (the look back sits on the final respond day), so the calendar.csv rows match.

## Lens checklist, scope and sequence layer

| Line | Met? |
|---|---|
| Unit question answerable without the unit's sources, or one defensible answer | Met: all nine questions are open and need the unit's data |
| History out of time order with no reason | Not applicable (history is retaught in brief inside economics days) |
| A contested event with one telling | Met: both lines on minimum wage, trade, tax fairness, policy |
| Writing from sources once a year or never builds short to long | Part met (finding 7) |

## Candidate cells

| Cell | Settled in the draft | My read |
|---|---|---|
| Marginal thinking (unit 1) | Kept inside T1.2, day 2, 0 days | Right |
| Consumer and producer surplus (unit 2) | Dropped to an extension | Right |
| Costs of production (unit 3) | Kept inside T3.6, day 22 | Right |
| Externalities on the graph (unit 4) | Kept inside T4.1, day 28 | Kept, moved to day 30 (finding 3) |
| Types of unemployment (unit 5) | Kept inside T5.2, day 38 | Right |
| Money creation (unit 6) | Kept inside T6.3, day 46 | Right |
| Pay stub and withholding (unit 8) | Kept inside day 60 | Right |
| First tax return (unit 8) | Kept, 1 day, day 64 | Right |
| Renting a first home (unit 8) | Dropped to an extension | Right |
| Paying for college (unit 9) | Kept, 1 day, day 72 | Kept at 0 days, riding in days 71 and 76 (finding 1) |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Portfolio observations dated across years from a made-up series built on published long-run asset-class returns | Four consecutive school days show noise, not why values rise and fall over time (PFL.T3.7) | data/plans/economics/days.csv rows 74 to 77 notes |
| Externalities on the graph moved from day 28 to day 30 | Day 28 holds two lessons; day 30 needs a worked case | days.csv rows 28, 30 |
| Depression retrieval dropped from day 28 | Retrieved again on days 37 and 47 | days.csv row 28 |
| T6.3's banks and institutions moved to day 45 | Day 46 holds two lessons; day 45 gains the readiness check's time | days.csv rows 45, 46 |
| Unit 9 day swap: paying for college rides in days 71 and 76; day 72 is financial markets and assets, day 73 diversification and research; T2.3 to day 68 | Splits the 5-code day 73 inside unit 9's days | days.csv rows 68 to 73, 76; scope-and-sequence.md unit 9 |
| CER model retrieved on day 16; day 49 a one-page written argument | First claim day; the course's best argument prompt | days.csv rows 16, 49 |

## For Cory

None. (The readiness call in finding 2 changes the frame's wording, not its units, days or standards.)

## Sources

- data/standards/ma-hss-2018.txt (Massachusetts 2018, ids and our words): every code checked against the days.
- C3 Framework (NCSS 2013, rev. 2017), D2.Eco.10 wording: from memory, not re-fetched; the progression row's word list
  agrees.
- CEE Voluntary National Content Standards in Economics (2010) and NSPFE 2021: from memory, for the load reasoning.
- Algebra II frame (docs/courses/algebra-ii/frame.md) and data/plans/calendar.csv: the A-SSE.B.4 timing.

Confidence: findings 1, 3, 5, 6 likely; 2 and 7 judgment calls; 4 likely; 8 firm.
