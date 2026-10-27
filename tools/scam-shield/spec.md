# Covered: Insurance Claims
Renamed from: Scam Shield

## One idea
The cheapest insurance depends on the year you end up having: compare three renters quotes side by side, slide the deductible to trade a lower monthly premium for more risk, and a year chart shows what each quote really costs in a quiet year, a stolen-laptop year and a kitchen-fire year; then use your own policy page as the answer key to catch fake "claim refund" texts that get your policy wrong.

## Not like
- phishing-spotter (CS 6-8, specced): fast keep-or-report rounds where you tap the visual tell (a look-alike address, a rush). Here a slow, careful round where you check each message against facts only you know (your insurer, your policy number, your one real claim) and tap the line on your own policy page it contradicts.
- capture-the-flag (CS 9-12, specced): finding and patching holes in a company's systems. Here no systems, only your own policy and your own inbox.
- e-bike-buyer (CTE 6-8, not built): one purchase and whether to add a warranty, insurance or a repair fund as bike crashes and thefts come up. Here no purchase story and no bike: quotes, deductibles and claim math for renters and auto policies, side by side.
- first-apartment-budget (9-12, money, built): renters insurance is one $15 line among many. Here the policy itself is the subject.
- the-credit-card-diaries (9-12, money, this group): four years of credit choices. Here no timeline; three possible years computed side by side.
- paycheck-decoder, compound-interest-head-start (this group): pay and saving; no risk.
The overlap pass suggested this reshape ("Covered") to move away from an escape room on scams beside capture-the-flag, and away from a "year of surprises" that would repeat first-apartment-budget and the-credit-card-diaries. Taken, with the topic word added to the title, and the scam round tied to the policy page so it is not phishing-spotter's mechanic.

## Who and how
- Grade 9-12, career and technical education (personal finance), module "Insurance and Protecting Yourself".
- Topic line: insurance, deductibles and scam texts
- Driver: students on laptops, alone or in pairs. 20 to 40 minutes.
- Standards: NSPFE.Managing Risk (insurance types, premiums and deductibles, identity theft and scams).
- Data as of line: "Quotes and insurers are made up for learning. How deductibles, limits and actual cash value work follows the NAIC and the Insurance Information Institute (2025)."

## Screens and modes
Header: title, topic line, modes (`.seg`): `Quotes` (default), `Claims`, `Real or fake?`; then `Read`, `Motion`, `Sound`.

**Quotes.** Stage: three quote cards side by side (stacked below 760 px), each like a real quote sheet: insurer name and made-up logo shape, coverage (personal property limit), how it pays ("Replacement cost: pays what it costs to buy new" or "Actual cash value: pays what your things were worth, after wear"), deductible, monthly premium, yearly premium.
- `Deductible` slider under the cards with four stops ($250, $500, $1,000, $2,500); all three cards update together.
- Under the cards, the Year chart: three groups of bars (Quiet year, Stolen laptop, Kitchen fire), one bar per quote, each split into Premiums (solid) and You paid at claim time (striped). The cheapest bar in each group gets a "lowest" tag (word plus a check icon).
- Tap a quote card: `Pick this one` marks it as your policy (used by Claims and Real or fake?). Panel: the plain-word glossary (Premium, Deductible, Limit, Replacement cost, Actual cash value, Claim), each opening a one-line card.

**Claims.** The claim calculator. Panel: `Policy` select (your renters pick, or the auto collision policy), its own `Deductible` slider, and loss buttons (Content). Stage: one wide bar for the loss split into "Insurer pays" and "You pay", with the math under it in steps ("Laptop worth new: $900. Actual cash value after 3 years: $360. Minus deductible $250 = insurer pays $110. You pay $790."). When the loss is at or under the deductible, the stage says "Below your deductible: the insurer pays $0. Many people don't file small claims." `File claim` (only for a loss you choose to file) gives a claim number on your policy page (used in Real or fake?); one claim can be filed per visit.

**Real or fake?** Stage: a phone with a message inbox (10 messages, one at a time) beside your policy page (insurer, policy number, how the insurer contacts you, your filed claim if any, your deductible). For each message:
- Two buttons: `Matches my policy` or `Does not match`. For `Does not match`, then tap the line on the policy page it contradicts (a policy line is a 44 px button), or `Asks for something no insurer asks` (a card number, a password, a gift card, a fee to release a refund).
- Feedback names the fact ("Your insurer is Pinecrest Mutual; this says Pinecrest Refund Center" / "You have no open claim, so there is no claim refund"). No points; a running "checked 6 of 10" count.
- After the last message, the card `If you already clicked` lists the steps from the FTC (Content).

## Content
**Renters quotes** (made-up insurers; monthly premium at deductible $250 / $500 / $1,000 / $2,500):
- Pinecrest Mutual: replacement cost, limit $20,000: $19 / $16 / $13 / $10.
- Little Fox Insurance: actual cash value, limit $20,000: $13 / $11 / $9 / $7.
- Saltmarsh Insurance Co.: replacement cost, limit $10,000: $15 / $12 / $10 / $8.

**Renters losses** (replacement cost / actual cash value): stolen phone, 2 years old, $700 / $350; laptop stolen from a car, 3 years old, $900 / $360; kitchen fire damages belongings, $6,500 / $3,900; burst pipe upstairs ruins most belongings, $14,000 / $8,400. Note on the laptop: personal property coverage usually covers belongings away from home, too.

**Year chart** (premiums for 12 months plus what you paid at claim time; Quiet / Stolen laptop / Kitchen fire):
- $250: Pinecrest $228 / $478 / $478; Little Fox $156 / $946 / $3,006; Saltmarsh $180 / $430 / $430.
- $500: Pinecrest $192 / $692 / $692; Little Fox $132 / $1,032 / $3,232; Saltmarsh $144 / $644 / $644.
- $1,000: Pinecrest $156 / $1,056 / $1,156; Little Fox $108 / $1,008 / $3,708; Saltmarsh $120 / $1,020 / $1,120.
- $2,500: Pinecrest $120 / $1,020 / $2,620; Little Fox $84 / $984 / $5,184; Saltmarsh $96 / $996 / $2,596.
(The burst pipe in Claims shows the limit: Saltmarsh at $250 pays $9,750 and you pay $4,250, because its limit is $10,000.)

**Auto collision** (one made-up policy on a used car worth $6,000; monthly at $250 / $500 / $1,000 / $2,500: $92 / $80 / $66 / $48). Losses: backed into a pole $700; fender bender, your fault, $2,400; car totaled, $6,000 actual cash value (auto pays actual cash value). Card: "Collision covers your car in a crash. Liability, which most states require, covers damage you do to others." 

**Messages** (all made up; the policy page says: Pinecrest Mutual, policy PM-48213, "We contact you in our app or from 800-555-0142, and never ask for card numbers or passwords by text", deductible as chosen, claim CL-20931 if filed, else "No open claims"):
1. Real: "Pinecrest Mutual: your claim CL-20931 has a new update. Open the Pinecrest app to see it." (Only real if a claim was filed; if none, it does not match: no open claim.)
2. Fake: "PINECREST REFUND CENTER: you are owed $412.60 on an overpaid claim. Confirm your card number to receive it." (no such refund; asks for a card number)
3. Real: "Pinecrest Mutual: your policy PM-48213 renews on Aug 1. Your premium stays the same. Details in the app."
4. Fake: "Little Fox Insurance: claim approved! Pay a $25 release fee to get your $1,100." (wrong insurer; a fee to release money)
5. Fake: "Your Pinecrest policy PM-48231 will be canceled in 1 hour unless you verify your login here: pinecrest-verify.example" (wrong policy number; asks for a password)
6. Real: "Pinecrest Mutual: an adjuster will call you from 800-555-0142 about claim CL-20931." (real only with a filed claim)
7. Fake: "Insurance refund dept: send the $60 deductible in gift cards and we'll speed up your claim." (gift cards; deductibles are never paid that way)
8. Fake: "Pinecrest: your deductible went up to $5,000. Reply with your date of birth to keep your old rate." (contradicts your deductible; asks for personal data)
9. Real: "Pinecrest Mutual: we got your payment of $(premium). Thank you." (the amount matches your premium)
10. Fake: "Call 900-555-0199 now about your accident claim." (no accident claim; not your insurer's number)

**If you already clicked** (FTC, IdentityTheft.gov): report it at IdentityTheft.gov and get a recovery plan; change the passwords you may have shared; call your card company or bank to block the card; place a free fraud alert or credit freeze with the credit bureaus; check your free credit reports.

## Interactions in detail
- Claim math: value basis = replacement cost or actual cash value per the policy; insurer pays max(0, min(limit, basis) - deductible); you pay = replacement cost - insurer pays (what it costs you to replace everything). The steps show each number.
- Year chart = 12 x monthly premium + you paid at claim time; recomputed on every slider move; ties tag all tied bars.
- Messages 1 and 6 change answer with the filed claim; the checker reads the current policy page, and the feedback quotes the line it used. If the student picks a policy other than Pinecrest, the insurer name, number and phone on the policy page change, and messages are rewritten from the same templates so the real ones still match (the fake ones always contradict something).
- `Does not match` without tapping a reason asks "Which line on your policy page doesn't match?" and waits; any contradicting line counts (some fakes contradict two).
- No timers, no scores, nothing stored. `Start over` (panel) clears the pick, the claim and the inbox.
- Esc closes glossary cards; Tab order: slider, quote cards, chart groups; in Real or fake?, the two buttons, then the policy lines.
- Sizes: cards at real pixels; at 680x425 the chart shows one group at a time with `Quiet`, `Laptop`, `Fire` tabs; at 375 the phone and policy page stack, policy first.

## Look
- Accent `--brand #45d0e6` (calm cyan: slider thumb, Pick this one, active mode), `--brand-ink #04262c`. Base `kit/theme-912.css`.
- Quote cards on light sheets (`#f7f9fb`, ink `#18212b`, muted `#56606c`) so they read like paper quotes; Premium bars `#45d0e6`, You paid bars `#f2a65a` striped; the phone dark `#0b0f14` with message bubbles `#e9eef3`.
- Contrast: accent on panel 9.41:1, on `--sec-bg` 8.92:1; brand-ink on accent 8.66:1; sheet ink 15.4:1, muted 6.3:1 on the sheet; bubble text `#18212b` on `#e9eef3` 13.9:1.
- Differs from this group's other accents (yellow, spring green, raspberry, coral, violet, orange, trail green, periwinkle) and from capture-the-flag's pink and phishing-spotter's lime.

## Art
none: drawn in code (quote sheets, simple logo shapes from circles and leaves, chart, phone).

## Voice
Bank voice `news-reader` (Rasalgethi), "Say clearly and steadily, like a trusted radio news reader": a steady consumer-protection tone, not alarm. Not used by another tool in this group or a 9-12 CTE tool. `Curio.voice`, `scope: () => state.mode`. Messages are on screen only (Read speaks them).
- welcomeQuotes (how): "Slide the deductible and watch all three quotes change. Then compare the three kinds of year."
- pickHow (how, first chart change): "Tap Pick this one on the quote you would buy."
- welcomeClaims (how): "Pick a loss to see who pays what."
- belowDeductible (event, a loss at or under the deductible; stale on the next loss): "That loss is below your deductible, so the insurer pays nothing."
- welcomeFake (how): "Check each message against your policy page. Tap Matches, or tap Does not match and the line it gets wrong."
- caught (event, a correct Does not match; stale on the next message): "Right. It gets your (fact) wrong."
- clicked (event, after the last message): "If you ever click one, there are clear steps. They're on the screen."

## Family engine
The money family engine, described in full in paycheck-decoder's spec. This tool uses `money` and `r2` only; the claim math is this tool's own (no sibling needs it).

## Sources
- Premium, deductible, limit, replacement cost and actual cash value, filing small claims: NAIC, "A Consumer's Guide to Renters Insurance" and Auto Insurance consumer guides (https://content.naic.org/consumer), and Insurance Information Institute, "Renters insurance" and "What is covered by standard renters policies?" (https://www.iii.org/insurance-basics/renters-insurance).
- Personal property covered away from home: Insurance Information Institute, renters coverage (https://www.iii.org/article/renters-insurance).
- Collision versus liability coverage; auto claims pay actual cash value: Insurance Information Institute, "What is covered by a basic auto insurance policy?" (https://www.iii.org/article/what-covered-basic-auto-insurance-policy).
- Scam signs (refund and fee scams, gift cards, requests for card numbers or passwords) and recovery steps: FTC, "How to Recognize and Avoid Phishing Scams" (https://consumer.ftc.gov/articles/how-recognize-and-avoid-phishing-scams), "Paying scammers with gift cards" (https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams) and IdentityTheft.gov (https://www.identitytheft.gov/).
- Fraud alerts and free credit freezes: FTC, "Credit Freezes and Fraud Alerts" (https://consumer.ftc.gov/articles/what-know-about-credit-freezes-fraud-alerts).
- 555 phone numbers, insurers, quotes, policy and claim numbers, losses: made up for this tool (800-555-01xx and 900-555-01xx are fictional ranges).

## Done when
1. Quotes at $500: yearly premiums $192, $132, $144; the year chart matches every Content value at all four deductibles.
2. Lowest tags: at $250, Quiet is Little Fox ($156), Stolen laptop and Kitchen fire are Saltmarsh ($430).
3. Claims: laptop on Little Fox at $250 gives insurer $110, you $790; burst pipe on Saltmarsh at $250 gives insurer $9,750, you $4,250; phone at $1,000 on any policy says below deductible.
4. Auto: fender bender at $1,000 gives insurer $1,400, you $1,000; at $2,500 insurer $0; totaled at $500 gives $5,500.
5. Messages 1 and 6 count as real only after a claim is filed; without one, their contradicting line is "No open claims".
6. Changing the picked policy rewrites the policy page and messages so each real message still matches.
7. Every fake message names the policy line or "asks for something" it contradicts, and the If you already clicked card lists the FTC steps.
8. Cards, slider and chart are visible without scrolling at 1366x768; the 680x425 preview shows the cards and one chart group.
9. How lines once each in five actions in a row; belowDeductible and caught every time, dropped when stale.

## Open questions
- Title: the note's "Covered" plus the topic word gives "Covered: Insurance Claims". Fine, or another title (the old "Scam Shield" would point at the smaller part)?
- The quotes and insurers are made up, so no real premium data is shown (real renters premiums vary widely by state). OK to keep the numbers made up but realistic, with the "made up for learning" line?
