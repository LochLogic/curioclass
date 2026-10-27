# The Credit Card Diaries

## One idea
Live four years of Remy's life from 18 to 22 as a diary with two facing pages: the left page is what happened (a choice about a card, a loan or a phone plan), the right page is Remy's credit report, which writes each choice down in a lender's words and keeps it for years, so at 22, when a landlord reads that right-hand page, you see your whole story the way a stranger sees it.

## Not like
- first-apartment-budget (9-12, money, built): one year of a full budget, with a credit score as a side gauge. Here credit is the whole story, over four years, and the report itself is on screen line by line.
- paycheck-decoder (9-12, money, this group): one pay stub, no choices. Here choices and their long tail.
- compound-interest-head-start (9-12, money, this group): interest working for you. Here interest working against you (card interest, loan interest in school).
- scam-shield (9-12, money, this group): insurance and fake messages. Here only real lenders, and the free credit report check in chapter 14 is the only overlap (identity errors).
- workplace-scenarios (CTE 6-8, story): choices ripple across one workday on a timeline map. Here choices ripple across four years into a document.
- interest-rate-dial (CTE 6-8, not built): one dial and four people. Here one person and many small decisions.

## Who and how
- Grade 9-12, career and technical education (personal finance), module "Credit and Debt".
- Topic line: credit scores, cards, loans and student debt
- Driver: students on laptops, alone or in pairs; the teacher can project chapter 1 and vote as a class. 30 to 45 minutes for all 16 chapters; any chapter can be revisited.
- Standards: NSPFE.Managing Credit (credit reports and scores, card costs, loans, student debt).
- Data as of line: "Card rate about 24 percent (typical first card, 2026). Federal student loan rate 6.39 percent (2025-26). The score is a teaching model, not a real one."

## Screens and modes
Header: title, topic line, modes (`.seg`): `Diary` (default), `Report`, `Rewind`; then `Read`, `Motion`, `Sound`.

**Diary.** Stage: an open journal spread drawn in code. Left page: the chapter's date and Remy's age ("September, first year. Age 18."), the diary entry (2 to 4 sentences, first person) and the choice as 2 or 3 large option cards, each with its cost in plain numbers ("Student card: $500 limit, 24 percent APR. A hard credit check."). Right page: Remy's credit report as a lender sees it: Score box (or "No score yet"), Accounts (each with type, opened, limit or original amount, balance, and a row of payment marks, one per month: ✓ on time, 30 late, CO collections), Inquiries (with dates), and a Money strip: Checking, Savings cushion, Card balance, Student loan, Interest paid so far.
- Choose an option card: a short "what happened next" line appears under it, the three months play on the right page (month marks fill in one by one, about 1.5 seconds; instant with Motion off), and any new report line slides in with a highlighter mark and a margin note in a lender's words ("New account: revolving, limit $500.").
- `Next chapter` turns the page. `Card plan` (a small form on the right page, changeable between chapters): `Pay in full`, `Pay the minimum`, `Pay $100`.
- A ribbon of 16 tabs along the journal's edge shows chapters done.

**Report.** The right page full size, with a `Why this score?` panel: the five factors as bars (Payment history, Amounts owed, Length of history, New credit, Credit mix), each with its weight, its 0 to 100 value, and the lines on the report that set it. Tap a factor: the lines that feed it glow. A note at the top: "Real scoring models are secret and differ. This teaching score uses the published weights so you can see how each line counts."

**Rewind.** Every chapter as a row: the choice made, the score after it and the card balance after it. `Change this choice` reopens that chapter and replays the story from there (later choices are kept where they still exist, and the ones that no longer fit are asked again). A small line chart of score by chapter, the old path dashed, the new path solid.

End of chapter 16 (The apartment): the landlord's screen (made-up policy, shown on a clipboard): score 670 or more, deposit one month's rent; 580 to 669, two months; below 580 or no score, three months or a cosigner. Then a summary: total card interest paid, student loan balance with interest accrued, inquiries, late marks, and the line "These marks stay: late payments for 7 years, hard inquiries for 2." `Play again` (clears the run) and `Rewind`.

## Content
**Money each month** (spare cash after Remy's needs, into checking): first year $150, second $175, third $200, fourth $250. Starting checking $400. Card APR 24 percent; late fee $32 (money engine constants).

**Chapters** (three months each; date, entry gist, options and effects):
1. Sep, year 1 (18). Orientation card table. A Student card ($500 limit; hard inquiry; new revolving account). B Secured card ($200 deposit from checking held by the bank; $200 limit; hard inquiry; new revolving account; deposit returned when closed or upgraded). C No card yet.
2. Dec, year 1. Phone plan. A Postpaid unlimited with a new phone on a payment plan: $75 a month (in this story the carrier runs a hard credit check, and with no score asks a $150 deposit, returned in chapter 13). B Prepaid plan, keep the old phone: $30 a month. Either way it comes out of spare cash.
3. Mar, year 1. Textbooks $340. A On the card. B From checking. C Rent used copies, $120 from checking.
4. Jun, year 1. Summer job adds $100 a month for this chapter. Checkout offer: "Save 15 percent today with a store card." A Open it ($300 limit; hard inquiry; the $200 purchase becomes $170 on it). B No thanks, $200 from checking.
5. Sep, year 2. The bill is $3,000 more than aid covers. A Federal unsubsidized loan $3,000 at 6.39 percent (no credit check; installment account; interest accrues in school). B Private loan $3,000 at 11 percent with a parent as cosigner (hard inquiry; installment account; interest accrues). C Work 8 more hours a week this year (no loan; diary notes being tired; spare cash +$80 a month for the year).
6. Dec, year 2. Card company offers a higher limit. A Accept ($1,500; a soft check, not on the report as a hard inquiry). B Decline. (With no card: "A starter card offer arrives": A apply, $500, hard inquiry; B wait.)
7. Mar, year 2. Spring break trip $600. A On the card. B From savings and checking (blocked with a note if not enough). C Skip it, $0.
8. Jun, year 2. A friend says to set up autopay. A Autopay for at least the minimum (never late from now on). B Not now. If B and a card balance exists, the July payment is missed while Remy is away (late mark on the card, $32 fee).
9. Sep, year 3. A used car for the commute. A Auto loan $5,000 at 13 percent for 48 months ($134.14 a month; hard inquiry; installment). B A $2,500 older car from savings (blocked if short). C Keep the bus pass, $0.
10. Dec, year 3. Holiday gifts $250. A On the card. B From checking. C Make gifts, $40.
11. Mar, year 3. An urgent care bill of $400 arrives after insurance. A Call and set up a payment plan, $50 a month (nothing goes on the report). B Ignore it (it goes to a collection agency, which calls; because medical collections under $500 are not reported by the national credit bureaus, it does not show on the report; the diary notes the calls and that the debt is still owed).
12. Jun, year 3. "I never use my first card. Close it?" A Close it (the limit leaves the utilization math; the account stays on the report as closed in good standing). B Keep it open with one small subscription on autopay.
13. Sep, year 4. Pay-later at checkout for $200 headphones, 4 payments of $50. A Use it (not on this report while paid on time; a missed one would go to collections). B Card. C Wait and save, buy in December from savings.
14. Dec, year 4. Check your free credit reports. A Check them: one shows a late payment that isn't Remy's (another person with a similar name); Remy disputes it and it is removed next chapter. B Skip it: the wrong late mark stays and counts.
15. Mar, year 4. Graduation. The report and Money strip show the student loan with interest added (capitalized) after the 6-month grace period; the standard 10-year payment is shown. A Pay $50 extra a month toward it. B Standard plan. (No loan: "No student loan payments.")
16. Jun, year 4 (22). The apartment application, landlord's policy above. No choice: the landlord reads the report.

**Report wording** (margin notes): "Revolving account opened", "Installment account opened", "Hard inquiry", "Payment 30 days late", "Account closed by consumer, paid as agreed", "Collection account" (never for chapter 11's under-$500 bill), "Dispute resolved: item removed".

## Interactions in detail
- Months are simulated one at a time with the money engine's `statement()`: interest r2(balance x 0.24 / 12) only when last month's statement was not paid in full; minimum = min(balance, max($35, r2(1 percent of balance + that month's interest))); `Pay in full` pays the whole statement, `Pay $100` pays max(minimum, $100) capped at the balance. Payments come from checking, then the savings cushion; if both together cannot cover the minimum, the payment is late: $32 fee added to the card and a 30 mark.
- Spare cash goes to checking each month; anything over $300 in checking moves to the savings cushion at month end.
- Student loans (A or B in chapter 5): interest accrues at a simple daily-equivalent monthly rate (principal x rate / 12) from September of year 2 through the 6-month grace after graduation (26 months) and is added to the balance at repayment. Federal $3,000: $415.35 accrued, balance $3,415.35, standard payment $38.59 a month for 120 months. The private loan uses 11 percent the same way.
- The teaching score (shown once the oldest account is 6 months old; before that "No score yet: not enough history"):
  - Payment history PH = min(100, 70 + 2.5 x on-time months on the report) - 30 per late mark in the last 24 months - 15 per older late mark - 40 per reported collection; floor 0.
  - Amounts owed AO by card utilization (all open card balances / all open card limits at the last statement): under 10 percent 100; under 30 percent 85; under 50 percent 65; under 75 percent 40; 75 percent or more 15; no open card 70.
  - Length LH = min(100, round(average age of all accounts on the report in months x 100 / 120)).
  - New credit NC = 100 - 15 per hard inquiry in the last 12 months - 10 per account opened in the last 6 months; floor 0.
  - Mix MX: revolving only or installment only 60; both 100.
  - Score = round(300 + 5.5 x (0.35 PH + 0.30 AO + 0.15 LH + 0.10 NC + 0.10 MX)), 300 to 850.
- Blocked options (not enough money) stay visible, dimmed, with the reason, and cannot be chosen; there is always at least one option that can be.
- Chapter 8 with B and a $0 card balance: no payment was due, so nothing is missed; the diary says so.
- Rewind replays deterministically from the changed chapter (no randomness anywhere).
- Saves the run on this device (localStorage `credit-card-diaries-run`, try/catch); `Play again` clears it.
- Esc closes the Why panel; Tab order: option cards, Next chapter, Card plan, then report lines.
- Sizes: the journal spread at real pixels; at 680x425 and below 760 wide the pages stack with the left page first and a `See report` jump; at 375 wide the report lines become a list.

## Look
- Own light `:root` (a paper journal): `--paper #fbf7ee`, `--panel #fffdf8`, `--ink #2a2320`, `--muted #6b5e57`, `--line #e6dccb`, `--btn #a3245e`, `--head-ink #ffffff`, `--focus #1d4ed8`. Accent `--brand #a3245e` (raspberry ink: chapter tabs, option card borders, highlighter on new report lines is `#ffe2ef` behind ink text).
- Report page `#ffffff` with a light gray grid `#e3e6ea`, monospace numbers; marks ✓ `#1d6b3a`, 30 and CO `#a3241a` with their letters (never color alone).
- Contrast: accent on paper 6.61:1, on panel 6.95:1; white on accent 7.07:1; ink on paper 14.8:1; muted on panel 5.9:1; mark colors on white 6.6:1 and 7.0:1.
- Differs from first-apartment-budget (cream, navy, terra) and this group's dark tools; the only other light tools in the group are interview-simulator (gray office, coral) and path-planner (map paper, green).

## Art
none: drawn in code (journal spread, report grid, clipboard).

## Voice
Bank voice `big-sister` (Leda), "Say in a friendly, youthful way, like a helpful older student": Remy reading their own diary. Not used by another tool in this group or a 9-12 CTE tool. `Curio.voice`, `scope: () => state.mode`. Diary entries are voiced (they are the story; 16 entries, each under 200 characters, written by the builder from the Content gists); report lines are on screen only.
- welcomeDiary (how): "Read the left page, then tap one choice. Watch the right page: that's your credit report."
- planHow (how, first time a card exists): "Set your card plan on the right page. You can change it between chapters."
- entry1 to entry16 (event, when each chapter opens; stale if the page turns first): the chapter's diary entry.
- late (event, every late mark): "A payment was late. That mark stays on the report for seven years."
- firstScore (event, first time a score appears): "Remy has a score now: (score)."
- welcomeReport (how): "Tap a factor to see which lines on the report set it."
- welcomeRewind (how): "Tap Change this choice on any chapter to see a different path."
- landlord (event, chapter 16): "The landlord read the report. Deposit: (months) months of rent."

## Family engine
The money family engine, described in full in paycheck-decoder's spec. This tool uses `statement()`, `CARD_APR`, `LATE_FEE`, `loanPay`, `money` and `r2`. It feeds it: the 16 chapters, the monthly spare cash, and the loan terms; the teaching score lives in this tool (no sibling needs it).

## Sources
- Score factor weights (payment history 35, amounts owed 30, length 15, new credit 10, mix 10 percent): myFICO, "What's in my FICO Scores" (https://www.myfico.com/credit-education/whats-in-your-credit-score); the brand is not named on screen.
- A score needs at least six months of history: myFICO, minimum scoring criteria (https://www.myfico.com/credit-education/credit-scores/minimum-requirements-for-a-fico-score).
- Late payments stay up to 7 years; hard inquiries 2 years: CFPB, "How long does negative information remain on my credit report?" (https://www.consumerfinance.gov/ask-cfpb/how-long-does-negative-information-remain-on-my-credit-report-en-323/) and FTC, Credit Scores (https://consumer.ftc.gov/articles/credit-scores).
- Medical collections under $500 are not reported by the three national bureaus (since April 2023): CFPB, medical debt and credit reports (https://www.consumerfinance.gov/about-us/blog/medical-debt-anything-already-paid-or-under-500-should-no-longer-be-on-your-credit-report/).
- Free credit reports and disputes: FTC, Free Credit Reports (https://consumer.ftc.gov/articles/free-credit-reports) and CFPB, disputing errors (https://www.consumerfinance.gov/ask-cfpb/how-do-i-dispute-an-error-on-my-credit-report-en-314/).
- Federal undergraduate loan rate 6.39 percent for 2025-26, unsubsidized interest accrues in school, 6-month grace: Federal Student Aid (https://studentaid.gov/understand-aid/types/loans/interest-rates, https://studentaid.gov/understand-aid/types/loans/subsidized-unsubsidized).
- Card APR about 24 percent and $32 late fee: money engine constants from first-apartment-budget (Federal Reserve G.19 average about 22 percent for accounts assessed interest, https://www.federalreserve.gov/releases/g19/current/).
- Secured cards, store cards, pay-later plans and soft versus hard checks: CFPB Ask CFPB articles on secured cards and buy now pay later (https://www.consumerfinance.gov/ask-cfpb/).
- Remy, the landlord policy, the offers and the prices: made up for this tool.

## Done when
1. Textbooks on the card ($340, Pay the minimum, no earlier balance): month payments $35, $35, $35; interest $0.00, $6.10, $5.52; balance after the chapter $246.62, interest paid $11.62.
2. Trip on the card ($600, minimum): balance $517.13 after three months, interest $22.13.
3. Teaching score checks: PH 85, AO 100, LH 5, NC 85, MX 60 gives 712; PH 100, AO 85, LH 20, NC 85, MX 100 gives 751; PH 70, AO 40, LH 20, NC 70, MX 60 gives 589.
4. No score shows until the oldest account is 6 months old; choosing C in chapter 1 and B in chapter 2 keeps "No score yet" until a first account ages.
5. Federal loan path: $415.35 accrued, $3,415.35 at repayment, $38.59 a month; auto loan $134.14 a month.
6. Chapter 8 B with a balance adds one late mark and $32; with a $0 balance it adds nothing.
7. Chapter 11 B never adds a collection line; chapter 14 A removes the wrong late mark in chapter 15 and the score rises by the PH rule.
8. Rewind changes one choice and replays to a matching end state every time (same inputs, same report).
9. The spread, option cards and Next chapter are visible without scrolling at every STANDARDS.md size.
10. How lines once each in five actions in a row; late, firstScore, entries and landlord every time they happen, dropped when stale.

## Open questions
- Remy's report lines use lender wording ("Collection account", "Payment 30 days late"). Some teachers may want the story to end in a happy deposit either way; the landlord policy can end at three months or a cosigner. OK as written?
- Chapter 11 states that unpaid medical bills under $500 do not appear on credit reports (the bureaus' 2023 policy). That policy could change; keep it with the "as of" date in the teacher notes, or use a non-medical bill?
