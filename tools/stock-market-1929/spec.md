# Stock Market 1929

## One idea
Buy the real 1929 Dow with borrowed money and watch your own margin account through the actual closes: the loan that
multiplied the boom is the same loan that let the broker sell you out, then replay the same days under the rules
written after the crash.

## Not like
- inflation-wallet: prices rise and money melts in 1923 Germany; here prices fall and a debt you took on does the damage.
- market-time-machine (built, grades 9-12): yearly returns, asset mixes and long horizons since 1928; here one account,
  one event, day by day closes, leverage and margin calls, no asset mix and no "stay invested" lesson.
- fed-chair: you set interest rates as policy; here you are one borrower, and the only rules switch is a law that was
  actually passed.
- concert-ticket-market (same format, built): curves from a teaching model with a bright stage; here a real time series
  on a dark ticker-tape instrument, no curves, no invented demand.
- economy-dashboard: browse many macro series; here one series you live inside with your own money on the line.

## Who and how
Grade 11, social studies (US history, Roaring Twenties and the Great Depression). Driver: students on their own laptops,
or a teacher on a projector. 20 to 40 minutes. Standards: D2.His.14.9-12, D2.Eco.12.9-12.

## Screens and modes
Header: title "Stock Market 1929" with the ticker-machine picture small at its left, `.seg` mode buttons **Ride the
market**, **Two rule books**, **What changed**, then icon buttons Motion (`motion`), Sound (`sound`), Read (`read`).
Layout: kit stage plus panel. Under about 900 px tall the panel goes buttons-first (Play, Pause, Next day, Speed, Sell
everything at the top, setup chips below).

### Ride the market (opens here)
- Focus: the Dow line growing day by day and, right under it, your account bar. Together they fill the stage (the chart
  about two thirds of the stage height, the bar the rest); the panel holds only setup chips, readouts and buttons.
- Stage: a large line chart of the Dow close (y axis 0 to 400, x axis from the chosen start to 12/31/1932), drawn up
  to the current day only. Under it, a stacked bar for the account: your share (equity) in green, the broker's loan in
  grey, and a dashed horizontal "call line" marker. A ticker strip across the top of the stage shows the date and close
  as plain code text on the painted tape-strip ("OCT 29 1929   DOW 230.07   DOWN 11.7 PERCENT").
- Before Play the chart shows its axes and the start point only, with the start close on the tape.
- Panel, before Play:
  - **Start day** chips: **Jan 1928**, **Jan 1929**, **Peak: Sep 3, 1929**, **Oct 23, 1929**.
  - **You put down** chips: **100 percent (no loan)**, **50 percent**, **25 percent**, **10 percent** (default 10).
  - **Rules** chips: **1929 rules**, **Today's rules**. Choosing Today's rules forces You put down to 50 or 100 and greys
    out 25 and 10 with the note "Regulation T: at least 50 percent down."
  - Fixed: your cash $1,000 in the account, plus $500 savings at home for margin calls. A small line under it: "$1,000
    in 1929 is about $18,000 in 2024 dollars."
  - Readouts: Stock value, Loan, Your share, Your share as a percent, Savings left, Loan interest rate this month.
  - Buttons: **Play**, **Pause**, **Next day**, **Speed** (1x, 4x), **Sell everything**, **Reset**.
- While playing, each step reveals the next close (see Content for steps). Event markers pop up as small cards on the
  chart (Content, Events); the four voiced events carry a small painted picture (Art). Hint paragraph (`hint`) explains
  the current state in one sentence.
- **Margin call** card (playback pauses): it opens over the lower part of the stage, covering the right side of the
  account bar, with the chart still visible above it and the phone cutout at its left; the eye goes here. Text:
  "MARGIN CALL. Your share has fallen to X percent. Your broker needs $N to bring it back to Y percent." Buttons:
  **Pay from savings ($N)** (disabled with "Not enough savings" if N > savings), **Let the broker sell**, **Sell
  everything**. A checkbox **From now on, let the broker sell** answers future calls automatically.
- **Account statement** (end of data, Sell everything, wiped out, or closed under $1): a card centered on the stage over
  the dimmed chart, its text in code on the painted statement-paper, the ticker-machine picture in its corner. It shows
  start day, rules, down payment, highest your share reached and when, the day it ended, cash returned or "You owe the
  broker $N", what the same $1,000 would be with no loan on the same day. Buttons: **Try another down payment** (same
  start, back to setup), **Reset**.

### Two rule books
- Focus: the one chart with the two account lines; the two mini statements sit in the panel and stay small.
- Same start day chips. Two accounts run together on one chart: **1929 rules, 10 percent down** (amber line) and
  **Today's rules, 50 percent down** (green line), each line showing that account's share in dollars, with the Dow
  as a faint grey line behind on its own right axis. Both start with $1,000; calls are answered "broker sells"
  automatically and marked with a small labelled tick on that account's line ("call", "sold", "closed").
- Buttons: **Play**, **Pause**, **Next day**, **Speed**, **Reset**. Side panel: two mini statements updating live, plus
  a no-loan $1,000 readout for reference.
- Takeaway card once both finish (or the data ends), centered on the stage over the chart: one computed line per
  account (Peak start: "1929 rules: first forced sale Sep 20, 1929; closed Oct 28, 1929 owing $18.12." and "Today's
  rules: first forced sale Oct 29, 1929; still open with $3.08."), then the fixed text: "Both accounts lost money. The
  50 percent rule did not stop the losses. It gave the account room: the forced sales came later and were smaller, and
  no single bad day wiped it out." (Checked for all four start days, see Sources.)

### What changed
- Focus: the open card, large in the middle of the stage (its painted picture on the left; date, title, text, excerpt
  and "Connects to your account" on the right). A horizontal timeline strip 1929 to 1934 with the seven card titles
  runs along the bottom of the stage; the panel holds the hint, and the Try it button when card 7 is open.
- Tap a card on the timeline strip to open it (Content, Reforms). Keyboard: left and right arrows move between cards.
- One card, **Margin rules**, has a **Try it** button that switches to Ride the market with Today's rules and 50
  percent down already chosen.
- No quiz, no points.

## Content

### Price data: Dow Jones Industrial Average closes (317 points)
Weekly rows are the last close of each week (Mon to Sat). From 9/3/1929 to 11/27/1929 every trading day is included.
Two extra points are added: 12/31/1929 and the all-time-low 7/8/1932. One step of playback = the next row. The chart
x axis is real calendar time, so daily steps sit closer together. Store as one array `[["1928-01-07",201.45],...]`.

- 1928 Jan-Jun: 1/7 201.45, 1/14 199.51, 1/21 198.06, 1/28 200.31, 2/4 196.30, 2/11 199.02, 2/18 192.48, 2/25 193.15, 3/3 194.53, 3/10 201.32, 3/17 204.70, 3/24 208.56, 3/31 214.45, 4/5 212.12, 4/14 216.93, 4/20 210.90, 4/28 212.25, 5/4 217.66, 5/11 220.74, 5/18 217.64, 5/25 217.74, 6/2 220.27, 6/9 211.51, 6/16 205.96, 6/23 204.25, 6/30 210.37
- 1928 Jul-Dec: 7/7 212.49, 7/14 207.83, 7/21 209.95, 7/28 215.66, 8/4 216.15, 8/11 214.91, 8/18 222.41, 8/25 233.68, 9/1 240.41, 9/8 241.72, 9/15 239.62, 9/22 239.37, 9/29 237.38, 10/6 240.17, 10/13 249.13, 10/20 253.75, 10/27 255.51, 11/3 254.16, 11/10 265.58, 11/17 277.48, 11/23 288.22, 12/1 290.80, 12/8 257.33, 12/15 270.72, 12/22 285.94, 12/29 297.28
- 1929 Jan-Jun: 1/5 302.43, 1/12 301.25, 1/19 305.96, 1/26 314.56, 2/2 319.76, 2/8 301.53, 2/16 295.85, 2/21 310.06, 3/2 319.12, 3/9 311.61, 3/16 320.00, 3/23 306.21, 3/28 308.85, 4/6 302.81, 4/13 304.41, 4/20 311.07, 4/27 315.68, 5/4 327.08, 5/11 324.59, 5/18 321.48, 5/25 304.33, 6/1 299.12, 6/8 305.12, 6/15 314.26, 6/22 322.23, 6/29 333.79
- 1929 Jul-Aug: 7/6 344.66, 7/13 345.94, 7/20 345.87, 7/27 343.73, 8/3 355.62, 8/10 344.84, 8/17 360.70, 8/24 375.44, 8/30 380.33
- 1929 Sep-Nov daily: 9/3 381.17, 9/4 379.61, 9/5 369.77, 9/6 376.29, 9/7 377.56, 9/9 374.93, 9/10 367.29, 9/11 370.91, 9/12 366.35, 9/13 366.85, 9/14 367.01, 9/16 372.39, 9/17 368.52, 9/18 370.90, 9/19 369.97, 9/20 362.05, 9/21 361.16, 9/23 359.00, 9/24 352.61, 9/25 352.57, 9/26 355.95, 9/27 344.87, 9/28 347.17, 9/30 343.45, 10/1 342.57, 10/2 344.50, 10/3 329.95, 10/4 325.17, 10/5 341.36, 10/7 345.72, 10/8 345.00, 10/9 346.66, 10/10 352.86, 10/11 352.69, 10/14 350.97, 10/15 347.24, 10/16 336.13, 10/17 341.86, 10/18 333.29, 10/19 323.87, 10/21 320.91, 10/22 326.51, 10/23 305.85, 10/24 299.47, 10/25 301.22, 10/26 298.97, 10/28 260.64, 10/29 230.07, 10/30 258.47, 10/31 273.51, 11/4 257.68, 11/6 232.13, 11/7 238.19, 11/8 236.53, 11/11 220.39, 11/12 209.74, 11/13 198.69, 11/14 217.28, 11/15 228.73, 11/18 227.56, 11/19 234.02, 11/20 241.23, 11/21 248.49, 11/22 245.74, 11/25 243.44, 11/26 235.35, 11/27 238.95
- 1929 Dec: 12/7 263.46, 12/14 253.02, 12/21 235.42, 12/28 238.43, 12/31 248.48
- 1930 Jan-Jun: 1/4 248.85, 1/11 248.71, 1/18 246.84, 1/25 259.06, 2/1 268.41, 2/8 269.78, 2/15 269.25, 2/21 265.81, 3/1 273.24, 3/8 275.46, 3/15 270.25, 3/22 276.43, 3/29 286.19, 4/5 289.96, 4/12 293.43, 4/17 294.07, 4/26 285.46, 5/3 258.31, 5/10 272.01, 5/17 272.41, 5/24 271.33, 5/29 275.07, 6/7 257.82, 6/14 244.25, 6/21 215.30, 6/28 219.12
- 1930 Jul-Dec: 7/3 222.46, 7/12 229.23, 7/19 236.65, 7/26 240.31, 8/2 234.50, 8/9 222.59, 8/16 228.02, 8/23 234.42, 8/29 240.42, 9/6 243.64, 9/13 240.34, 9/20 229.85, 9/27 212.52, 10/4 211.10, 10/11 193.05, 10/18 185.29, 10/25 193.34, 11/1 184.89, 11/8 173.14, 11/15 186.68, 11/22 188.04, 11/29 183.39, 12/6 178.37, 12/13 163.34, 12/20 169.42, 12/27 160.30
- 1931 Jan-Jun: 1/3 172.12, 1/10 171.71, 1/17 162.89, 1/24 169.80, 1/31 167.55, 2/7 172.90, 2/14 180.41, 2/21 191.32, 2/28 189.66, 3/7 183.85, 3/14 180.76, 3/21 185.24, 3/28 174.06, 4/4 172.43, 4/11 168.03, 4/18 162.37, 4/25 151.98, 5/2 147.49, 5/9 151.31, 5/16 142.95, 5/23 137.90, 5/29 128.46, 6/6 129.91, 6/13 137.03, 6/20 138.96, 6/27 156.93
- 1931 Jul-Dec: 7/3 155.26, 7/11 143.88, 7/18 142.42, 7/25 138.24, 8/1 136.65, 8/8 134.94, 8/15 145.80, 8/22 137.76, 8/29 142.08, 9/4 132.62, 9/12 123.85, 9/19 111.74, 9/26 107.36, 10/3 92.77, 10/10 105.61, 10/17 102.28, 10/24 109.70, 10/31 105.43, 11/7 115.60, 11/14 106.35, 11/21 97.42, 11/28 90.02, 12/5 90.14, 12/12 78.93, 12/19 80.75, 12/24 75.84
- 1932 Jan-Jun: 1/2 74.62, 1/9 79.98, 1/16 84.44, 1/23 77.98, 1/30 76.19, 2/6 74.45, 2/13 85.82, 2/20 83.59, 2/27 82.02, 3/5 88.49, 3/12 84.52, 3/19 78.09, 3/26 75.69, 4/2 71.30, 4/9 64.48, 4/16 63.39, 4/23 59.22, 4/30 56.11, 5/7 58.04, 5/14 52.48, 5/21 53.04, 5/28 47.70, 6/4 50.88, 6/11 48.26, 6/18 47.55, 6/25 44.76
- 1932 Jul-Dec: 7/1 44.39, 7/8 41.22, 7/9 41.63, 7/16 45.29, 7/23 47.84, 7/30 54.26, 8/6 66.56, 8/13 63.19, 8/20 67.18, 8/27 75.61, 9/3 78.33, 9/10 76.54, 9/17 66.44, 9/24 74.83, 10/1 72.09, 10/8 61.17, 10/15 64.22, 10/22 60.85, 10/29 62.09, 11/5 62.41, 11/12 68.04, 11/19 64.14, 11/26 58.89, 12/3 55.83, 12/10 61.25, 12/17 60.11, 12/24 57.98, 12/31 59.93

Daily changes to show on the ticker (computed from the rows above, rounded to 0.1): 10/28/1929 down 12.8 percent,
10/29/1929 down 11.7 percent, 10/30/1929 up 12.3 percent. Peak 381.17 on 9/3/1929; low 41.22 on 7/8/1932, 89 percent
below the peak. First close above 381.17 again: 382.74 on 11/23/1954 (shown as a note in the statement, not plotted).

### Loan interest: New York call money rate, monthly average, percent per year
- 1928: 4.24, 4.38, 4.47, 5.08, 5.70, 6.32, 6.05, 6.87, 7.26, 6.98, 6.67, 8.60
- 1929: 7.05, 7.06, 9.10, 8.89, 8.91, 7.70, 9.23, 8.23, 8.50, 6.43, 5.44, 4.83
- 1930: 4.64, 4.32, 3.69, 4.00, 3.12, 2.62, 2.20, 2.21, 2.19, 2.00, 2.00, 2.23
- 1931: 1.57, 1.50, 1.55, 1.52, 1.45, 1.50, 1.50, 1.50, 1.50, 2.10, 2.50, 2.70
- 1932: 2.65, 2.50, 2.50, 2.50, 2.50, 2.50, 2.08, 2.00, 2.00, 1.35, 1.00, 1.00

### Events (cards on the chart, at the row with that date or the next row after it)
- 8/9/1929: "The New York Fed raises its discount rate to 6 percent to cool borrowing."
- 9/3/1929: "The Dow closes at 381.17, its 1920s peak."
- 10/24/1929: "Black Thursday. Panic selling; bankers try to steady prices. Close 299.47."
- 10/28/1929: "Black Monday. Down 12.8 percent in one day."
- 10/29/1929: "Black Tuesday. Down another 11.7 percent."
- 10/30/1929: "A one-day bounce of 12.3 percent. It does not last."
- 11/13/1929: "The 1929 low: 198.69, almost half gone since September."
- 4/17/1930: "A rebound high of 294.07. Many think the worst is over."
- 6/17/1930: "The Smoot-Hawley Tariff becomes law, raising tariffs on imports."
- 12/11/1930: "The Bank of United States in New York closes. Bank failures spread."
- 9/21/1931: "Britain leaves the gold standard."
- 7/8/1932: "The bottom: 41.22, 89 percent below the peak."
- 11/8/1932: "A new president is elected, promising a New Deal."

### Account model (one marked block, `MARGIN ACCOUNT MODEL`)
- Buy at the start row's close: stock value = $1,000 / down fraction; loan = stock value minus $1,000. Units =
  stock value / close. The account holds "the Dow" as if it were one stock (say so in a note).
- Each step: loan grows by (call rate of the previous row's month / 100) x (calendar days since previous row) / 365.
  Then value = units x close, share = value minus loan, share percent = share / value.
- Call line: 1929 rules = half your down payment (10 down calls at 5, 25 at 12.5, 50 at 25). Label it in the UI as
  "a typical broker rule in this model; in 1929 no law set it." Today's rules = 25 percent (FINRA maintenance minimum).
  100 percent down: no loan, no calls, ever.
- On a call: Pay from savings adds N = (down fraction x value) minus share, which pays down the loan. Let the broker sell
  sells stock worth X = value minus (share divided by down fraction) and uses it to pay down the loan, restoring your down percent.
- If share is 0 or less at any step: the broker sells everything; if the sale does not cover the loan, the statement
  says "You owe the broker $N" (N = minus share). Account closed; playback stops.
- Sell everything: share is paid out as cash, loan repaid, account closed, statement shows.
- If share is under $1.00 after any step (and above 0): the broker closes the account and pays the share out as cash;
  the statement says "Closed: your share fell under $1."
- At 50 percent down the two rule books give the same call line (25 percent); Today's rules differ by forbidding 25 and
  10 percent down.
- Savings never earn interest. No taxes or commissions (say so in a note).

### Reforms (What changed cards)
1. Oct 1929, "Borrowed money". "Most buyers put down about 10 percent and borrowed the rest, with the stock as the
   loan's backing. No law set a limit." Connects: "This is the 10 percent chip."
2. Mar 1933, "Bank holiday". "Banks across the country were closed for days so they could be checked before reopening."
   Connects: "Your loan came from a broker, who borrowed from banks."
3. May 27, 1933, "Securities Act of 1933". "Companies selling new stock must register it and tell buyers the facts."
   Excerpt from its title: "To provide full and fair disclosure of the character of securities sold in interstate and
   foreign commerce and through the mails, and to prevent frauds in the sale thereof". Connects: "In 1929 you bought
   with little required information."
4. June 16, 1933, "Banking Act of 1933 (Glass-Steagall)". "Separated ordinary banking from selling securities and
   created the FDIC." Connects: "Banks could no longer gamble deposits in the stock market."
5. Jan 1, 1934, "Deposit insurance begins". "The FDIC insures each depositor up to $2,500." Connects: "Savings in an
   insured bank were now safe even if the bank failed. Your $500 savings would have been covered."
6. June 6, 1934, "Securities Exchange Act of 1934". "Created the Securities and Exchange Commission to police the
   markets and gave the Federal Reserve power over margin." Excerpt from Section 7: "For the purpose of preventing the
   excessive use of credit for the purchase or carrying of securities". Connects: "This is the law behind Today's rules."
7. "Margin rules over time". "The Fed's Regulation T started Oct 1, 1934. Its first fixed rule, 55 percent down, came
   Apr 1, 1936. Since Jan 3, 1974 it has been 50 percent. Brokers today must also keep your share at 25 percent or more."
   Button **Try it**. Also show: "US unemployment reached 24.9 percent in 1933."

## Interactions in detail
- Setup choices lock when Play is pressed; Reset unlocks them. Changing Rules to Today's while 25 or 10 is chosen
  moves the down payment to 50.
- Playback: 1x = 4 rows per second, 4x = 16 rows per second. Next day advances one row while paused (it is disabled
  while playing, and no line names it then). With Motion off, the line still advances step by step (it is data pacing)
  but the chart does not animate between points, cards appear without sliding and the phone does not shake.
- Run length: 47 s (Oct 23) to 79 s (Jan 1928) at 1x, plus voiced holds. Kept: the slow 1930 to 1932 grind is the
  lesson for no-loan and 50 percent accounts; 10 percent runs close within about 15 s, and 4x takes 20 s or less.
- Controls stay live while playing: Pause stops on the current row at once, Speed changes the rate from the next row,
  Sell everything closes the account on the current row and opens the statement, and the mode buttons stop playback
  and speech. A tap is never held for the next row.
- Event cards: up to 3 visible; older ones fade to small dots on the line that reopen on click or Enter. Pressing an
  event card does not pause playback; a margin call always pauses.
- Voiced market events (Black Thursday, Black Monday, Black Tuesday, the bottom): at 1x with Sound on, playback holds
  on that row until the line ends (about 5 s), with its card shown larger; Pause, Speed (4x ends the hold), Sell
  everything and Read still respond at once. At 4x or with Sound off there is no hold and the card only shows. Each
  plays once per run.
- If a market event and an account event land on the same row (Black Monday and a 10 percent account closing), the
  market line plays first, then the account line, then the statement line if it was never heard.
- Extremes: the Jan 1929 start at 10 percent down gets its first call on Black Thursday (10/24) and is wiped out on the
  next row (10/28) owing $89.65. The Oct 23 start at 10 percent gets no call at all: its share is 7.9 percent on
  10/26, above the 5 percent line, and the 10/28 gap takes it straight to owing $486.11. Multiple calls in a row each
  pause unless the auto-sell box is ticked. Pay button shows exact dollars to the cent and disables when savings are
  short. A share that crosses zero between rows (gap down) produces the "owe" statement, never a negative bar: the bar
  shows 0 share and a red "owed" stub below the axis.
- A share under $1.00 closes the account (Content, Account model). Reaching 12/31/1932 open: the statement says
  "Still open on Dec 31, 1932".
- Two rule books: both accounts step together on the same rows; a closed account's line stops with a "closed" tick.
  Its call, sold and closed ticks are silent (text on the chart only).
- What changed opens on card 1. Try it keeps the start day the student last used.
- Keyboard: Space = Play/Pause, Right arrow = Next day, all buttons focusable with visible focus, 44px targets. Colors
  are never the only signal: lines are also labelled at their ends, and call ticks carry text. Moving focus to the
  margin call card or the statement uses `focus({preventScroll: true})`.
- Sound starts on (kit default). localStorage (try/catch): last mode only. Nothing to copy, print or move between
  devices.

## Look
9-12 dark instrument. Link `kit:curio`, then `kit:theme-912`; `--brand` is ticker green `#3ccf7e` (9.32:1 on `--paper`
`#0d1219`, 8.59:1 on `--panel` `#141b25`; button text `#08180f` on it 9.08:1). The account share bar and the Today
line use the brand green; the loan bar and the faint Dow line are grey `#8a96a8` (6.27:1 on paper); the 1929 account
line is amber `#f2a93b` (9.41:1); the owed stub is red `#ff8a7a` (8.2:1). Statement text `#1e1a14` on the paper's
cream `#efe6d2` (13.95:1, muted `#5a5040` 6.37:1); ticker text `#1b1b1b` on the tape's `#ece4cf` (13.59:1). Painted
art is a muted period palette (sepia, brass, ink green), unlike market-time-machine's brass and teal editorial look
and concert-ticket-market's indigo and magenta. Readout numbers in the theme's readout font. No confetti, no score, no
win screen: every run ends in a plain account statement, never "you beat the crash".

## Art
Local FLUX (`scripts/localart.py`) for all 15 images; none has people (people no on every one), so none waits on
Gemini. Every prompt ends with the style "muted period oil painting, sepia, brass and ink green, low warm light".
Surfaces that would carry print are asked for blank; all text stays in code. Cutout no unless marked.
- ticker-machine: "A 1920s brass stock ticker machine under a glass dome on a dark wooden desk, a curl of blank white
  paper tape spilling from it, plain dark background"; 1:1; cutout yes; beside the header title, statement corner.
- tape-strip: "A long flat strip of blank cream paper ticker tape lying straight across a dark wooden surface, side
  light showing the grain"; 5:1; full-frame texture behind the ticker strip text.
- phone: "A 1920s black candlestick telephone with its earpiece on the hook, brass details, front view, plain white
  background"; 1:1; cutout yes; left of the margin call card, shakes briefly as the call opens (Motion on).
- statement-paper: "A sheet of blank aged cream paper with faint ruled lines and a thin border, lying flat, even soft
  light"; 3:4; full-frame background of the statement and the takeaway card.
- exchange-facade: "The columned stone front of the New York Stock Exchange on a narrow empty street at dawn, flags
  hanging still, wet cobbles"; 16:9; the Black Thursday card.
- board-room: "A 1920s brokerage customers' room, rows of empty wooden chairs facing a tall blank green chalkboard
  wall, one chair tipped over, loose papers on the floor, grey window light"; 16:9; the Black Monday card.
- floor-paper: "An empty 1920s stock exchange trading floor ankle deep in torn paper slips and ticker tape, tall
  trading posts with blank boards, dusty window light"; 16:9; the Black Tuesday card.
- cold-chimneys: "A row of brick factory chimneys under a flat grey winter sky, the air still and clear, bare trees and
  a frozen yard below"; 16:9; the July 1932 bottom card.
- certificates: "A small stack of ornate stock certificates with engraved green borders and blank centers, tied with a
  faded ribbon, a brass fountain pen beside them"; 4:3; What changed card 1, Borrowed money.
- bank-doors: "The tall closed bronze doors of a 1930s stone bank, a blank paper notice pasted on one door, fallen
  leaves on the steps, overcast light"; 4:3; card 2, Bank holiday.
- open-book: "A thick open bound book with blank cream pages, a brass magnifying glass resting on them, a green
  banker's lamp glowing"; 4:3; card 3, Securities Act.
- teller-window: "A closed brass bank teller's window grille on a polished marble counter, a small brass bell beside
  it"; 4:3; card 4, Banking Act.
- passbook: "A small closed savings passbook with a plain dark blue cover on a wooden table beside a short stack of
  silver dollars"; 4:3; card 5, Deposit insurance.
- capitol-dome: "The United States Capitol dome at dusk seen from a distance across a quiet lawn, sepia tones"; 4:3;
  card 6, Securities Exchange Act (kept from the first spec; savings-plan uses a vault door).
- balance-scale: "A brass balance scale on a dark wooden desk, an equal small stack of gold coins on each pan, the
  beam level"; 4:3; card 7, Margin rules.
Drawn in code (charts, bars and labels): the Dow chart, account bar, call line, ticks, two-line chart, timeline strip,
readouts and preview.svg. The 9 unvoiced event cards are text only.

## Voice
Bank `hs-narrator`, voice `Kore`, style "Read clearly and naturally, at a moderate pace" (kept: no tool `neighbors.py`
lists has a voice yet; the two built neighbors, market-time-machine and concert-ticket-market, have none). Uses
`Curio.voice` with scope `mode + ':' + runId`. Readouts, cards and the statement are read on screen; Read speaks the
hint. Event lines below are the explicit event set; the rest are how lines (spoken once per page load, then hint only).
1. welcome-ride (how; Ride entered; stale on Play): "It is nineteen twenty-nine, and you can buy stocks with mostly borrowed money. Tap a start day and a down payment, then press Play."
2. welcome-two (how; Two rule books entered; stale on Play): "Same days, two rule books. One account follows nineteen twenty-nine habits, the other follows today's law. Press Play and watch when the broker calls."
3. welcome-changed (how; What changed entered; stale when a second card opens): "After the crash, Congress wrote new rules for banks and markets. Tap a card on the timeline to see what changed, and why."
4. first-call (how; first margin call card when Pay is enabled; stale when the card closes): "Margin call. Your share of the account has fallen too low. Tap Pay from savings, or tap Let the broker sell."
5. call-short (how; first margin call card when Pay is disabled; stale when the card closes): "Margin call, and your savings cannot cover it. Tap Let the broker sell, or tap Sell everything."
6. call-again (event; every later margin call card; stale when the card closes): "Another margin call. Pick an answer on the card."
7. broker-sold (event; each broker sale in Ride, chosen or automatic; stale at the next call, the close, Reset or mode change): "The broker sold part of your stock to pay down the loan."
8. wiped (event; account closed with nothing owed and nothing left, or under $1; stale on Reset or mode change): "Your account is closed. The broker sold everything to pay back the loan."
9. owe (event; account closed owing money; stale on Reset or mode change): "Prices fell so fast that the sale did not cover the loan. You still owe the broker money."
10. black-thursday (event; 10/24/1929 row reached at 1x, Ride; stale when playback leaves that row, on Reset or mode change): "October twenty-fourth, nineteen twenty-nine. Black Thursday. Panic selling floods the exchange."
11. black-monday (event; 10/28/1929 row at 1x, Ride; stale as above): "October twenty-eighth. The Dow falls almost thirteen percent in a single day."
12. black-tuesday (event; 10/29/1929 row at 1x, Ride; stale as above): "October twenty-ninth. Another drop of nearly twelve percent. Brokers call in loans everywhere."
13. bottom (event; 7/8/1932 row at 1x, Ride; stale as above): "July eighth, nineteen thirty-two. The Dow closes at forty-one point two two, eighty-nine percent below its peak."
14. statement (how; first statement shown; stale when it closes): "Your statement is ready. Tap Try another down payment to run the same start again, and compare."
15. takeaway (event; Two rule books takeaway card appears; stale on Reset or mode change): "Both accounts lost money. The fifty percent account was sold out later and in smaller pieces, and no single day wiped it out."
Hints (silent after their line, spoken by Read): before Play "Tap a start day and a down payment, then press Play.";
playing "Press Pause to stop on this day, or Sell everything to cash out now."; paused "Press Play to go on, or Next
day to step one row."; call card as lines 4 or 5; statement as line 14.

## Family engine
none. Keep the account model and chart in clearly marked blocks (`MARGIN ACCOUNT MODEL`, `DOW CHART`) so they can be
lifted into a kit file later.

## Sources
- Dow closes 1928 to 1932 and the 11/23/1954 close: daily DJIA series in the `stevedata` R package (DJIA dataset;
  1914 to 1991 values from Pinnacle Systems), github.com/svmiller/stevedata, data/DJIA.rda. Peak 381.17 and low 41.22
  match Federal Reserve History, below.
- Call money rates: NBER Macrohistory series m13001, "Call Money Rates, Mixed Collateral, New York", via FRED
  M13001USM156NNBR, https://fred.stlouisfed.org/series/M13001USM156NNBR
- Typical 10 percent down, peak 9/3/1929 at 381.17, Black Monday nearly 13 percent, Black Tuesday nearly 12 percent,
  bottom 41.22 at 89 percent below the peak, New York Fed discount rate to 6 percent in August 1929: Federal Reserve
  History, "Stock Market Crash of 1929", https://www.federalreservehistory.org/essays/stock-market-crash-of-1929
- Regulation T dates and percents (Oct 1, 1934; 55 percent Apr 1, 1936; 50 percent Jan 3, 1974): Federal Reserve Board,
  "Margin requirements" historical table, https://www.federalreserve.gov/boarddocs/rptcongress/annual05/sec5/c1t08.htm
- 25 percent maintenance: FINRA Rule 4210 (Margin Requirements), https://www.finra.org/rules-guidance/rulebooks/finra-rules/4210
- Securities Act of 1933, Securities Exchange Act of 1934 (Section 7, 15 U.S.C. 78g) and their dates: SEC, "The Laws
  That Govern the Securities Industry", https://www.sec.gov/about/about-securities-laws ; statute text via
  https://www.govinfo.gov
- Banking Act of 1933, FDIC creation, $2,500 coverage from Jan 1, 1934: FDIC, "A Brief History of Deposit Insurance",
  https://www.fdic.gov/resources/publications/brief-history-deposit-insurance
- March 1933 bank holiday, Bank of United States closing 12/11/1930: Federal Reserve History essays "Banking Panics of
  1930-31" and "Banking Panics of 1933", https://www.federalreservehistory.org
- Smoot-Hawley Tariff signed 6/17/1930: US Senate, "The Smoot-Hawley Tariff", https://www.senate.gov
- Britain leaves gold 9/21/1931: Federal Reserve History, "Britain leaves the gold standard"
- 1933 unemployment 24.9 percent: Historical Statistics of the United States, series Ba475 (Lebergott)
- $1,000 in 1929 about $18,000 in 2024: BLS CPI-U annual averages 17.1 (1929) and 313.689 (2024), https://www.bls.gov/cpi/
- Number checks (Python, 2026-10-29 revision; the account model above run on the 317 rows and the monthly rates):
  - Data: 317 rows, increasing, no duplicates or Sundays. Ticker changes 10/28 -12.8, 10/29 -11.7, 10/30 +12.3
    percent: match. Low 41.22 is 89.2 percent below 381.17; 11/13 low 198.69 is 47.9 percent below ("almost half");
    CPI ratio gives $18,344 ("about $18,000").
  - Done when 1 to 5 all reproduce: Peak no-loan $157.23 (end) and $108.14 (7/8/1932); Peak 10 percent pay $487.15,
    $12.85 left, 9/30 unpayable; auto-sell sales 9/20, 9/30, 10/4, 10/23 then owe $18.12 on 10/28; Oct 23 start owes
    $486.11 on 10/28; Today's 50 percent first call 10/29/1929, open at the end with $3.08.
  - Fixed: the old extremes note said a call can fire on the next row after an Oct 23 start at 10 percent. It does
    not (share 7.9 percent on 10/26, then owing on 10/28 with no call); the Jan 1929 start now carries the example.
  - Fixed: the old takeaway said the first call comes "later and smaller" for every start, but the Oct 23 1929-rules
    account never gets a call. New wording checked on all four starts: Today's first forced sale is later (Jan 1928:
    4/25/1931 vs 11/12/1929; Jan 1929: 11/12/1929 vs 10/24/1929; Peak: 10/29 vs 9/20/1929; Oct 23: 11/13 vs the 10/28
    close) and smaller ($863, $754, $816, $708 vs $8,704, $6,943, $4,871 and a full close), the Today account is never
    wiped out, and both accounts end below $20 while no-loan ends at $157 to $297.
  - Added: the under-$1 close; 25 percent auto-sell runs otherwise sit open at $0.00 to $0.98 from late 1931 (Peak
    drops under $1 on 9/12/1931). No Done when result changes (smallest open account at the end is $3.08).
  - At 50 percent down, 1929 rules and Today's rules give identical runs (both call at 25 percent).
  - Run lengths at 1x: 79, 66, 57 and 47 s for the four starts; at 4x 20, 17, 14 and 12 s.

## Done when
1. Ride, Peak start, 100 percent down: no call ever; statement shows $157.23 on 12/31/1932, and $108.14 at the 7/8/1932
   low (within $0.01).
2. Ride, Peak start, 10 percent down, 1929 rules: first margin call on 9/20/1929 (close 362.05). Paying from savings
   costs $487.15 (within $1) and leaves $12.85; the next call on 9/30/1929 cannot be paid, its card says so and the
   call-short line never names Pay.
3. Same as 2 with the auto-sell box ticked: broker sells on 9/20, 9/30, 10/4 and 10/23/1929, then the account closes on
   10/28/1929 owing about $18 (within $1).
4. Ride, Oct 23 start, 10 percent down: no call; wiped out 10/28/1929 owing about $486 (within $1); the Black Monday
   line plays, then the owe line.
5. Ride, Peak start, Today's rules, 50 percent down: first call on 10/29/1929; with auto-sell the account is still open
   on 12/31/1932 with $3.08. 25 and 10 chips are disabled under Today's rules. A 25 percent auto-sell run closes with
   "Closed: your share fell under $1."
6. Two rule books, Peak start: the 1929 account closes on 10/28/1929, the Today account is still open at the end, and
   the takeaway card (with its computed lines) appears only after both finish.
7. Focus: at 1366x768 and 680x425 the Dow chart and account bar are the biggest thing on the Ride stage, the margin
   call card and the statement open over the stage (not in the panel), and the open What changed card is the biggest
   thing in that mode; Play, Pause and Sell everything are visible without scrolling at every size.
8. Tap while playing: at 1x, held clicks on Pause, Speed and Sell everything (including during a voiced hold on Black
   Thursday) take effect on the current row; Sell everything at once shows the statement for that row.
9. Every waiting line names an action and an enabled control; each how line is spoken once per load (five runs in a
   row: welcome and first-call once), event lines every time, and none plays after its moment has passed.
10. What changed: seven cards in date order, each with its painted picture, arrows move between them, Try it opens Ride
    with Today's rules and 50 percent.
11. No win screen, score, confetti or celebratory sound anywhere; every run ends in the statement. Motion off: no
    tweening, slides or phone shake, playback rate unchanged. Keyboard alone can run a whole ride and answer a call.
12. No em dashes in any visible text; the tool says "Curio Class" wherever it names the site.

## Open questions
- The under-$1 close is a new rule for the model (brokers did close tiny accounts, but the $1 line is this tool's
  choice). Keep it, or let those accounts run on to Dec 31, 1932 showing cents?
- Voiced market events now hold playback about 5 s each at 1x so the line matches the day on screen (up to about 20 s
  added). Keep the hold, or skip the voice during playback and show cards only?
- `hs-narrator` (Kore) is kept since no listed neighbor uses a voice yet, but it is a common voice across the site;
  `news-reader` (Rasalgethi, "trusted radio news reader") fits a 1929 ticker well if Cory wants this tool to sound
  different.
