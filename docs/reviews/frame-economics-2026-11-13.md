# Frame read: economics (Economics, with personal finance, half year), 2026-11-13

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/social-studies.md, section 1 of docs/ADOPTION-BAR-SUBJECTS.md,
  docs/courses/social-studies/STANDARD.md, docs/sources/BASE-TEXTS.md (social studies part).
- The frame docs/courses/economics/frame.md and its row in data/plans/frames.csv (9 units, 80 days).
- The 25 econ-* rows of data/progressions/social-studies.csv and every ss7-*, ss8-* and wh2-* row whose hands_on
  names an econ-* row.
- The frames before: docs/courses/civics-government-and-civic-life/frame.md (grade 8; ss8-public-budget) and
  docs/courses/world-geography-and-ancient-civilizations-ii/frame.md (grade 7; ss7-roman-economy). World History II has
  no frame yet, so its rows were read. The US History II frame (its unit 1 toolkit and the shared timetable).
- data/standards/ma-hss-2018.txt: MA.ECON.T1 to T7 and MA.PFL.T1 to T4, read line by line against the rows.
- The outline of Principles of Economics 2e on disk (S:\CurioClass-sources\openstax-retired-ccby\), against the
  frame's chapter map.
- Desk card q-ss-progression-1 (DESK-ANSWERS 2026-11-13): Economics open to grade 11 or 12, no US History I skill
  assumed.
- Earlier reads: docs/reviews/progression-social-studies-*2026-11-13.md (finding 4, grade 12 economics),
  progression-cross-*2026-11-13.md, frame-social-studies-kindergarten-2026-11-13.md, and my US History II and
  Government reads of today.
- Gates: `python -X utf8 scripts/plan.py check` (frame economics: 0 failures; 9 units, 80 days, 76 in units, 4 for
  checks) and `python -X utf8 scripts/stale.py check` (0 failures).

## Verdict

The frame is sound in design: all 25 econ-* rows are placed once, every ECON and PFL code is taught in full, the
anchor's order is kept with good reasons, the two supply and demand graphs are kept apart, and the personal finance
rules (made-up figures, no family questions, no real firms) are right. The biggest risk is time: the course carries
70 anchor codes in 76 unit days, and the year's informed action is squeezed into unit 8 beside three rows, while
unit 7 has about 3 teaching days for 11 codes. The one change that matters most is giving unit 8 its action days
and unit 7 one more day, taken from units 9 and 5, with a day budget for the check-set additions.

## Findings, most serious first

### 1. The year's informed action has no room in unit 8 (moderate; likely)

**What is wrong.** Unit 8 (7 days) holds econ-earning-income, econ-spending-consumer and econ-insurance-identity (7 PFL
codes, a first-year budget, made-up insurance quotes compared), a readiness check with a possible reteach of
ss8-public-budget, an end-of-unit assessment, a respond day, and the course's only informed action: choose a consumer
question, check it against public consumer-protection advice, make an information piece and share it through the
school. That leaves about 3 to 4 teaching days for three rows and the action. In Government the action has a whole
7-day unit.
**Why it matters.** Adoption-bar item 8 is scored; an action done in one rushed period reads as a poster, not as
students applying what they concluded to a problem near them.
**Fix (frame, units 8 and 9 rows).** Unit 8 to 9 days, unit 9 to 11 days: the frame's own "For the lead" item 1
names econ-credit and econ-borrowing-plan as the merge candidates, and they share one credit offer (credit card terms,
reports and disclosure, then the plan that compares offers and totals the cost), so unit 9 teaches them as one
running case over 4 days. State in unit 8's "What students learn": "the action takes 2 of the unit's days: one to
choose and research the question, one to make and share the piece; the look back is on the final check's respond
day". LAYER frame. REPEAT new.

### 2. Unit 7 has about 3 teaching days for 11 codes (moderate; likely)

**What is wrong.** Unit 7 (6 days) owns MA.ECON.T7.1 to T7.8, D2.Eco.14, D2.Eco.15 and D2.Geo.11: comparative advantage
worked from opportunity costs, tariffs and quotas, the free-trade argument weighed with evidence, the balance of trade
against the balance of payments, productivity compared across countries, exchange rates, and globalization's effects.
After the retrieval opener, assessment and respond day, about 3 days remain. The frame's "Unsure" would take a day
from unit 1, which already carries 12 codes in 8 days.
**Why it matters.** Comparative advantage and the balance of payments are the two ideas students most often get wrong
in a first course; three days cannot teach them and the free-trade argument T7.8 asks for.
**Fix (frame, units 5 and 7 rows; "Unsure" line).** Unit 7 to 7 days, unit 5 to 8 days: unit 5 has the lightest load
per day (8 codes in 9 days) and its "types of unemployment" addition rides inside T5.2's lesson on how unemployment is
counted. Delete the "Unsure" line's idea of taking the day from unit 1. Days stay 80. LAYER frame. REPEAT new.

### 3. The check-set additions have no day budget (moderate; likely)

**What is wrong.** Additions named: marginal thinking early (unit 1), consumer and producer surplus (2), costs of
production (3), externalities on the graph (4), types of unemployment (5), money creation through lending (6), the pay
stub, withholding, a first tax return and renting a first home (8), paying for college (9). Each is said to fit inside
the unit's days. Bar item 10 says additions never push the year past its days; C1 sets a 10 percent limit (about 7
days) on time outside the course's standards. In this course, the fullest of the three, there is no slack.
**Why it matters.** The writer of unit 8 or 9 will either drop an addition silently or overrun into the final check.
**Fix (frame, course in brief and each "Check set adds" cell).** Add: "Additions ride inside an owned code's lesson
where one fits; at most 4 days in the course are for additions with no home code." Mark: marginal thinking
(T1.2), costs of production (T3.6, which needs it), externalities (T4.1), types of unemployment (T5.2), money creation
(T6.3) and the pay stub and withholding (PFL.T1.1 and T1.2, the first-year budget) ride inside; paying for college (1
day, unit 9) and a first tax return (1 day, unit 8) take days; consumer and producer surplus and renting a first home
become extensions named in the unit plan. LAYER frame. REPEAT new.

### 4. Unit 2 uses financial markets before the course says what they are (minor; firm)

**What is wrong.** Unit 2 owns MA.ECON.T2.6 and T2.8 (equilibrium and its shifts "in product, resource and financial
markets"), but T2.11 (how financial markets move money from savers to investors) is placed in unit 9's econ-investing.
A grade 11 student has not had US History II's unit 1, where the idea appears.
**Fix (frame, unit 2 "What students learn").** After "the same reasoning in product, labor and financial markets" add
"(a financial market defined in one line: savers lend or buy shares, borrowers and firms pay a price for the money,
the interest rate or return; unit 9 teaches it in full)". No day change. LAYER frame. REPEAT new.

### 5. Row notes still lean on grade 11 (minor; firm)

**What is wrong.** "For the lead" items 2 and 3 name the "grade 12 courses" sentence and econ-taxes-budgets's 16th
Amendment note. More grade 11 wording remains, untrue for a grade 11 student since q-ss-progression-1:
- econ-business-forms: "Builds on the grade 11 rise of the corporation."
- econ-market-structures: "with the grade 11 trusts as a historical case".
- econ-government-role: "from the Sherman Act met in grade 11".
- econ-business-cycles: "the railroad booms and panics of grade 11".
- econ-money-banking: "the fight over a national bank met in grade 11".
- econ-markets-prices: "the supply-demand graph from grades 7 to 11".
- econ-scarcity-choice, econ-taxes-budgets, econ-earning-income, econ-trade, econ-global-economy: the "grade 12
  courses" clause.
Each row then adds "retaught here in brief", so the notes contradict themselves.
**Fix (data/progressions/social-studies.csv, next fix pass).** Drop each "met in grade 11" or "of grade 11" phrase so
the example reads as retaught in brief ("the trusts of the late 1800s, retaught in brief as a case"); "grades 7 to
10" for the graph; the frame's own wording for the "grade 12 courses" clause. LAYER progression. REPEAT yes
(progression-social-studies finding 9).

### 6. Stale status note (minor; firm)

data/plans/flow-status.csv, frame:economics: "active ... Writing: docs/pipeline/briefs/frame-write.md". The frame is
written and passes the gate. Fix: "Written; expert and Codex reads under way". The HANDOFF note that
q-ss-progression-1 is open for Cory is in the US History II read (finding 8). LAYER process. REPEAT yes (kindergarten
frame read finding 5).

## Checked and found right (do not undo)

- **Owned skills.** All 25 econ-* rows placed once; no econ-* row assumes a US History I or II row.
- **Standards in full.** MA.ECON.T1.1 to T7.8 and MA.PFL.T1.1 to T4.2 all placed and taught at their wording. D2.Eco.1
  to D2.Eco.15 and D2.Geo.11 match their rows (Eco.4's competition among buyers through monopsony; Eco.2's marginal
  argument with marginal benefit and cost defined first). The T4 split (budgets in unit 4, fiscal and monetary policy
  in unit 6) and T2.11 and T6.5 and T6.6 moved to personal finance each carry a reason.
- **Models.** Production possibilities, circular flow and aggregate supply and demand are introduced here and used
  again in the units the table names; the two supply and demand graphs are taught as different models with different
  axes.
- **Values.** Both lines of evidence on the minimum wage and on trade's winners and losers; tax fairness from backed
  sources; no party's policy presented as settled.
- **Personal finance rules.** Made-up offers, quotes, portfolios and brands; no family income or debt asked;
  bankruptcy and repossession taught without shaming; scams shown as patterns.
- **Partial bases.** The chapter map matches Principles of Economics 2e as it is ordered on disk (chapters 1 to 34
  checked); the CFPB activities with the agency's name and logo left out.

## Seams

From grade 7: ss7-roman-economy hands on to econ-money-banking, and the grade 7 frame names it. From grade 8:
ss8-public-budget hands on to five econ-* rows; the civics frame's hand-on table and this frame's seam table agree.
From grade 10: wh2-industrial-revolution, wh2-postwar-prosperity, wh2-great-depression, wh2-soviet-collapse and
wh2-globalization are picked up where the rows say. Beside it: US History II's unit 1 covers MA.USII.T1 economics as
a review; neither course assumes the other, and both frames say so. After: none; threads end here as stated. No
finding.

## Cross-subject

Math leans: Algebra I (graph features, growth by a constant percent) and math 7 (percent) as retrieval; Algebra II's
loan formula (A-SSE.B.4) has a local bridge (a given payment table), so the plan never depends on it. No same-year
lean is unbridged. No finding.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| An anchor standard in the course's Massachusetts topic range has no unit | Met: every ECON and PFL code placed |
| The replaced grade 3 year, or "your state" in grade 8, keeps Massachusetts-only content | Not applicable: no Massachusetts-only code in ECON or PFL |
| No unit lists what the check set adds, or an addition has no recorded source | Met for listing and source (unit 7 "none expected", to be confirmed by its table); days for additions missing (finding 3) |

## What I could not judge

- The California, Tennessee, New York and college-framework lines (not opened; checked at the unit plan).
- Whether the days hold in practice: findings 1 to 3 are read from the counts; the scope and sequence tests them day
  by day.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| The paying-for-college lesson centres on comparing aid offers and loan terms (with filing the aid form named) | In the suggested timetable a grade 12 student takes Economics in the spring, when aid offers arrive and are compared; filing is in the fall | docs/courses/economics/frame.md (unit 9 "Check set adds") |
| The trade unit's worked comparative-advantage case uses two made-up countries and two goods with whole-number labour costs, then one real pair from public trade data | Whole numbers keep the opportunity-cost arithmetic out of the way of the idea; the real pair meets D2.Eco.14 | docs/courses/economics/frame.md (unit 7) |

## For Cory

- **Personal finance inside a half year (audience).** The course gives personal finance about 20 days. Many states
  now require a separate half year of personal finance for graduation (from memory, about half the states by the
  2026-27 to 2028 graduating classes), so a school in one of them cannot use this course for that requirement. My
  pick: keep Economics as framed (it follows the anchor) and add a Personal Finance half year to the after-the-core
  list as a candidate, built mostly from the CFPB activities already in the source store. Yours, because it adds a
  course.

Not logged in the defect ledger: the brief allows edits to this report only. The caller may log findings 1 to 6
with found_by `expert`.

## Sources

- data/standards/ma-hss-2018.txt: every ECON and PFL code.
- S:\CurioClass-sources\openstax-retired-ccby\Economics2e-OP_s2jF42u.pdf, outline read with pypdf: chapter numbers
  for the frame's map.
- From memory: the C3 9-12 economics indicator wording; state personal finance graduation requirements (the
  Next Gen Personal Finance state tracker reports them; not opened for this read); the aid calendar (the federal aid
  form opens in the fall, offers arrive in spring).

## For the source list

- The Next Gen Personal Finance state policy tracker (ngpf.org), for the count of states requiring a personal finance
  course. Not opened in this read; needed before the "For Cory" item is decided.
