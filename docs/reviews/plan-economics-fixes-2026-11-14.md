# Economics unit plans: fixes from the two reads (2026-11-14)

Reads applied: the Claude expert read (docs/reviews/plan-economics-2026-11-14.md) and the Codex read
(docs/reviews/plan-economics-codex-2026-11-14.md). The expert's "For the fixer" list went first, in its order. Then
came every Codex finding the expert had not already covered. Every 2025 to 2026 fact was checked on November 14, 2026
against a primary source: the court, the agency, the law or the release. A fact that could not be confirmed is listed
under "Unverified" and is not written as fact.

Gate: `python -X utf8 scripts/unitplan.py check economics` passes all nine units. `scripts/sequence.py check economics`,
`scripts/plan.py check economics` and `scripts/frame.py check economics` show 0 failures. The day count (80) and the
unit totals are unchanged. There are no em dashes. No "?" characters remain where a letter or mark belongs.

## A change made to pass the word cap

The added material put seven units over the checker's 1,250-word cap. Two things brought them back under it.

- **The dated teacher background lines moved to frame.md.** These are the 2025 to 2026 law, court and rate lines for
  units 4, 6, 7, 8 and 9. They now sit in one new section, "Teacher background, as of November 2026", so the facts
  that change have one home. Each unit plan keeps a one-line pointer to its entry in field 2.
- **Prose was trimmed in fields 2, 3 and 7 to 10.** The cuts followed UNIT-PLAN.md's cut order: rule restatements,
  repeated supports and spare reasons. No check item, error, day row, key or source link was cut.

## Applied

### Expert read, "For the fixer", in order

| Finding | File | What changed |
|---|---|---|
| 1.1, CW1 | s01 field 4 | **"Given:" line.** The check now takes the last ten minutes of day 1, after the hook and the day's teaching. Economics opens on school day 81, and day 1 is the course's own first day. |
| 1.2 | s01 field 4 | **Five items.** The check is cut to five items: one item on budget, opportunity cost and the reason to fund together; one pollution graph; bonds; a three-measure panel; and Soviet pressures and queues. Results set the day 2 and day 3 groups. |
| 1.3 | s01, days.csv 2 and 3 | **Reteach blocks.** Day 2 has one ten-minute block on items 1 and 4. Day 3 has one block on items 2 and 3, after the frontier is taught. Day 6 gives ten minutes to item 5. The expert's item numbers (1 and 5, then 3 and 4) referred to the old order. The same split was kept after the items were renumbered. |
| 1.4, CW5 | s01 | **Item 7 shuffled**, with a new key. |
| 2 | days.csv 1, 2, 3, 6, 29, 30, 59, 69 | **Wording.** The day 1 note now reads "given in the last ten minutes of this day, after the hook". Notes now say "day 1's check" in place of "the start-of-year check". Reteach stations are added on days 2 and 3. Day 29's targeted support moved to day 30's opening (4.6). |
| 3 | scope-and-sequence.md | **Same wording change.** This file was named in the fixer list. It also falls under the brief's s*.md glob. |
| 7.1 | s07, frame.md | **Tariff line, dated** (frame.md, unit 7). It covers the February 20, 2026 ruling (Learning Resources v. Trump, with V.O.S. Selections, 6 to 3: the emergency powers law does not authorize tariffs). Section 232 duties stand, and the July 2026 section 301 tariffs are included. Copper: 50% on semi-finished products since August 1, 2025, on full value since April 6, 2026; the refined-copper phase-in is proposed only. Card F carries a real-world note. |
| 7.3, CW4 | s07 field 10 | **One voice per side.** Stone (steel) and a farm exporter's account, set beside the Market Facilitation Program records. The second steel voice (Wolfe) is dropped. |
| 7.4 | s07 | **Day 54's Depression comparison** is reduced to one teacher-read background sentence. |
| 7.5 | s07 | **Day 53 exit** now uses new goods and numbers: fruit and software support (US 6 and 2; Chile 4 and 8). |
| 7.6 | s07 | **Item 9's card** is labelled a discontinued, dated historical table. |
| 7.2 | s07 | **Day 56 minutes.** The expert proposed using day 57, but day 57 is the assessment. Day 56 was split instead: 5, 8, 12 (D2.Eco.15), 10 (D2.Geo.11 taught), 10 (closing claim) and 5. |
| 8.1 | s08, frame.md | **Tax year 2026.** Standard deduction $16,100 (Rev. Proc. 2025-32). A Schedule 1-A teacher line covers tips and overtime. A "check before teaching" line covers direct filing. **Made-up case:** wages 26,000, withholding 1,250, taxable income 9,900, table tax 993, refund 257, plus a separate identity-protection response. |
| 8.2, Codex 10 | s08 | **Item 3 and source B** now use the Blake, Nosko and Tadelis paid-search field experiment. Student copy names no company. Samples and error D are updated. The fraud chart moves to day 61 teaching. |
| 8.3 | s08 field 10 | **Informed-action scoring guide**: four rows scored 2, 1 or 0, with a meets sample and a does-not-yet-meet sample. |
| 8.4 | s08 | **Own error letter J** for "borrowing removes the cost", with its repair. |
| 8.5 | s08, frame.md | **Agency line** is an instruction only: check its status before teaching. The court details could not be confirmed (see "Unverified"). |
| 8.6 | s08 | **Age 27.** The expert's fixer list says "age 26", but the finding itself offers 27, which is clearly past the age-26 parent-plan limit. |
| 9.1 | s09 | **Source A** adds the audit office's August 2025 status: the deposit insurer's recommendation is implemented; the Federal Reserve's is open. Agency line as in 8.5. |
| 9.2 | s09, frame.md | **2025 law lines** (PL 119-21): new loan plans, Grad PLUS closed, Parent PLUS caps, 529 changes, and Trump accounts (section 70204, Form 4547, $1,000 pilot deposit). 2026 limits: IRA $7,500, employer plan $24,500. A third card on day 69 covers the child accounts. |
| 9.3 | s09 | **Dated reference rates** from G.19 (November 6, 2026, third quarter): card 22.36%, 60-month car 7.54%, 24-month personal 11.90%. |
| 9.4 | s09 | **Day 75:** 5, 10 for modelling the agencies' mandates, 25 and 5. |
| 9.6 | s09 | **Column renamed "Date"**, with a note that values are rounded from published returns. |
| 4.3 | s04, frame.md | **Dated lines.** PL 119-21 made the 2017 rates and the standard deduction permanent ($16,100 for 2026). The September 2, 2025 search-monopoly remedies are described with no company named. Hart-Scott-Rodino: the 2025 form was vacated February 12, 2026. |
| 4.1, CW4 | s04 field 10 | **Evidence first:** CBO distribution reports and IRS SOI tables. Analysis pair labelled by lean. One voice per side. The low-income movement's page moves to the sensitivity study. |
| 4.2 | s04 | **Day 32 reads two voices.** The closing-claim revision moves to day 34. |
| 4.4 | s04 | **IRS SOI historical table 23** (tax years 1913 to 2018) replaces the university course table. |
| 4.5 | s04 | **Sources A and D** are read aloud or cut to about 120 and 110 words. |
| 4.6 | s04, days.csv 29 and 30 | **Public-budget rebuild** moves to day 30's opening. The Depression reteach moves to day 31's opening. Day 29 keeps its teaching minutes. |
| 6.1, Codex 8 | s06 | **Fiscal evidence.** The closing claim adds the CBO ARRA estimates (February 20, 2015) and Taylor 2011, and the CARES Act serves as day 47's example. The 2008 minutes are for the hook only. Students cite one fiscal record and one central-bank record. |
| 6.2 | s06, frame.md | **Fed line:** target range 3.75 to 4% (held October 28, 2026, 10 to 2), Warsh chair since May 2026, Cook still a governor (Trump v. Cook, June 29, 2026), runoff ended December 1, 2025, reserve requirements zero. |
| 6.3 | s06 | **Dead unemployed-workers link** replaced with "choose a dated published collection in production". |
| 2.1, CW4 | s02 | **One voice per side** on rent and on wages, plus the neutral CBO report (July 2019). |
| 2.2 | s02 | **Day 15** keeps San Francisco and the Diamond study. New York moves to day 16 as a transfer case. The expert said day 17, which is the assessment. |
| 2.3 | s02 | **Item timing:** 6, 15, 7 and 12 minutes. |
| 2.4, CW5 | s02 | **Item 6 shuffled**, with a new key. |
| 3.1 | s03 | **Readiness item 1's key** accepts occupation aid and Korean War procurement for Japan. |
| 3.2 | s03 | **Day 23 minute plan:** 10, 15, 10, 5 and 10. Day 23 has no business-form task, so the fix was applied in spirit. |
| 3.3 | s03 | **The 1911 trust case** is named in the production record only. Teacher and student copy describe it without the company name. |
| 3.4 | s03 | **SBA link** now points to the current guide section. A US union source (the BLS release plus one union federation statement) replaces the UK one. |
| 5.1 | s05 | **Day 42:** 18, 10, 14 and 8. The productivity case becomes a teacher-read card. The price-index move proposed by the expert did not fit: day 42 has no such comparison, and day 43 is the assessment. |
| 5.2 | s05 | **Soskin's dates:** "(1921 to 2025)". |
| 5.3 | s05 | **Revision line:** September construction was revised to +16,000. |
| CW6 | all field 10 | **Tennessee phrase** applied in every unit. |

### Codex findings the expert did not cover

| Finding | File | What changed |
|---|---|---|
| 2 | s01 field 5 | **Compact response form.** Grids; items 8 and 11 share one paragraph and items 10 and 12 share one explanation; reading time counts inside the 40 minutes. |
| 3 | s02 day 11 exit | **Full schedules** for bread, gardening labor and loans; students find each equilibrium themselves. |
| 4 | s02 field 3 | **Handoff** now points to s03.md field 4, given verbatim on day 18. |
| 5 | s03 field 5 | **Allocation:** 10, 10, 8 and 12 minutes. Items 11 and 13 share one causal diagram. |
| 6 | s03 | **Food-sales denominator** stated in the card, the key and the record. |
| 7 | s04 | **Day 30 exit graph** fully specified. |
| 11 | s08 | **Day 65 minutes:** 10, 15, 10, closing claim 10 and exit ticket 5, as separate tasks. |
| 12 (cases) | s09 field 10 | **Made-up cases.** Day 72 aid offers with keys (net price 16,000 and 18,000; remaining 8,500 and 12,500). Day 72 teaching car offers. The day 70 running card. |
| 13 | s09 | **Day 69 evidence box** on the education card from GAO-13-64 (2010 survey). Item 4 look-fors and sample are updated. |

## Not applied

| Finding | Reason |
|---|---|
| Codex 1, 9, 12 (daily evidence and exit tickets in units 1, 8, 9) | **The expert's settled ruling binds** (and CW7): exit tickets belong to the section plan, so their absence is not a defect. The case material in Codex 12 was applied. Codex's own settled line, "map retained products before adding exit tickets", is left for the section plans. |
| Codex 10 (generator repair, then refresh model fields) | **Shared script.** scripts/unit_skeleton.py is a shared file, so the repair goes to the structure pass. No model field was changed. |
| Expert 2.5 (item 10's clerk shift) | **Judgment call.** The expert marked it a judgment call, and the item measures marginal benefit and cost as written. It was left alone. |
| Expert 6.4 (move the day 46 money-functions sort to day 47) | **Wrong day.** The functions sort is taught on day 45, not day 46, so day 46 does not carry it. |
| Expert 1.5, 8.7, 9.5 | **Nothing left to change.** 1.5 needs no change per CW7. 8.7 and 9.5 were covered by the days.csv wording change. |

## Unverified

None of these is written as fact. Each is either an instruction to check, or left out.

- **The consumer finance agency's funding and operations in 2025 and 2026.** Court orders were found only in law and trade press, not on the court's site. s08 and s09 say "check its current status before teaching".
- **A free federal direct filing service in the 2027 season.** Written as "check before teaching; do not tell students it is".
- **A section 122 import surcharge after the February 2026 ruling.** Not confirmed on a primary page; left out of the tariff line.
- **Any Federal Reserve rate change in September 2026.** Only the October 28, 2026 hold is written.
- **The 993 tax-table figure for tax year 2026.** It follows the table rule at 10% (the 10% bracket tops out at $12,400 in 2026), but the 2026 table is not published. The plan says to recheck it.
- **The appeal status of the September 2025 search-monopoly remedies.** Not written beyond the remedies date.

## For the structure pass

- **Word cap for merged documents.** UNIT-PLAN.md "Length" sets 1,800 words for a one-section merged document. scripts/unitplan.py applies 1,250 to every unit plan. All nine Economics units are one-section documents. These plans were cut to 1,250 so they pass the gate, but the page and the checker disagree.
- **Teacher background in frame.md.** Dated "as of" lines now have one home there, in a section named "Teacher background, as of November 2026". If this suits other courses, UNIT-PLAN.md and the frame template could name the section.
- **Plural-unit parsing (Codex).** scripts/unit_skeleton.py `frame_models()` misses plural unit references such as "Units 8 and 9". Use `unit_nums()`, then refresh the carried-model lines in units 7, 8 and 9.
- **One-section document contract (Codex).** The template, the writer brief and unitplan.py should agree on what must be complete in a merged document, and on where daily evidence belongs.
- **Checks beyond code presence (Codex).** A check could confirm that an item measures its code and that referenced inputs exist.
- **"What changed since 2024" (expert).** Writer and read briefs could require this check for every law, rate and agency named.
- **Per-code minutes (expert).** Days that introduce more than two codes (15, 23, 32, 42, 56, 75) could be required to show minutes per code.
- **Retired wording in other courses (expert).** The retired "start-of-year check" wording remains in other courses' days.csv notes and scope-and-sequence files. The readiness rule in UNIT-PLAN.md's header ("before the unit opens") and the unit 1 exception in unitplan.py should be read together.
- **Several fixes named the wrong day (expert).** 2.2 and 7.2 pointed at assessment days 17 and 57. 3.2, 5.1 and 6.4 described day content that is not there. A read brief could ask the reader to check days.csv before naming a day.

## For Cory

None.
