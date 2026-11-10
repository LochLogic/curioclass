# Startup Shares

## One idea
At a pitch fair in a school gym, five made-up young companies stand at their booths, each with a founder (labeled "illustration"), the problem they solve, what they risked (savings, a steady job) and an honest "what could go wrong" card: Mei's seaweed packaging, Tomás's farm drones, Priya's tutoring app, Kofi's bike-repair chain and Hana's battery recycler; the child splits a pretend $1,000 among them with sliders, or buys a basket of all five, and presses Fast-forward, and one possible ten years plays out year by year (the tutoring app folds in year 3, the battery recycler takes off in year 6); then the child runs 100 futures at once and sees a spread chart of outcomes for their split next to the basket's, and reads that in this model half of single picks end with nothing while all five fail together only about 3 times in 100, though the average result is about the same; each company's future card also shows the jobs and products it added to the town when its new idea met a real need; at the end the child sees that spreading money out doesn't make the best result bigger, but it makes the worst result much less likely, and that new ideas grow the economy when they meet real needs, so a student in grades 6 to 8 learns about investing, risk and diversification, and how innovation grows an economy.

## Not like
- market-time-machine (Grades 9-12, live): historical index data. Here made-up young companies and many futures.
- compound-interest-head-start (Grades 9-12, spec): savings growth. Here risk and spreading out.
- startup-booth (Grades 9-12, spec): running a business. Here investing in five.
- snow-season-prices (Grades 6-8, spec): running a shop. Here owning shares.

## Who and how
- Grades 6-8, Personal Finance (CTE explore), module "Startup Shares". Standards: NSPFE Investing (National Standards for Personal Financial Education, 2021); D2.Eco.7.6-8 (role of innovation and entrepreneurship in a market economy), C3 Framework.
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every booth and card. Controls 48 px or more.
- Five companies, five sliders and a basket button, one-future playback, a 100-future spread chart, future cards. Extra: Pitch panel (the class asks each founder one question on the projector). tool.json `modes: ["Invest", "Pitch panel"]`, `minutes: "20-30"`, `grades_label: "Grades 6-8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| NSPFE Investing | Split $1,000; run 100 futures; compare with the basket | the spread chart | 2 |
| D2.Eco.7.6-8 | Read each future card; name what the idea added | jobs and products in the town | 3 |

## Screens and modes
Header (kit): title "Startup Shares"; `Invest`, `Pitch panel`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** The gym pitch fair with five booths, a $1,000 jar, and the fair's host. The welcome is queued (`welcomeAfter: true`): "Pretend money, real lessons. Tap a booth to meet a founder." First hint: "Tap a booth."

**Booths (focus: the fair).** At 1366x768 the fair is left with the booth card right; at 680x425 the card is a sheet. Each booth card has the problem, the risk, and what could go wrong.

**Split.** Five sliders that always add to $1,000, or `Buy the basket` ($200 each).

**One future.** `Fast-forward` plays ten years; companies grow, stay flat or fold with a one-line reason.

**Many futures.** `Run 100 futures` draws a dot spread for the split and for the basket, with "ended behind", "about even" and "ended ahead" counts and how many ended at zero.

**Future cards.** For each company that grew, what it added to the town (jobs, a product); for each that folded, what was learned.

**Spread out (the aha).** Host: "The basket didn't make the best result bigger. It made losing everything much less likely."

**The end.** The split, the spread chart and the future cards. `Print` prints them.

**Pitch panel (extra).** Class questions.

## Content
- All companies and founders are made up; the tool gives no picks or advice and says so on the first screen.
- Outcome odds are set from published young-company survival rates and labeled "simulated".

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The split can be changed and futures rerun any time.
- Keyboard: Tab to booths, sliders (arrows move them), the basket, Fast-forward and Run 100 futures; Enter picks.
- With Motion off futures show final results without playback.

## Look
- Accent `--brand` #2c6a4f pitch-fair green (header, sliders, buttons); gold #f4c542 (the booth in focus, the basket); paper #eef6f2; ink #0a2218; muted #4b5752.
- Contrast (WCAG 2.1, computed): white on brand 6.40:1; brand on paper 5.82:1; ink on paper 15.22:1; muted on paper 6.86:1; ink on gold 10.29:1.
- Never color alone: ahead, even and behind carry words and dot shapes.
- Different from this batch (late-night indigo, clipboard teal, ski-lift red, crayon magenta).

## Art
- People (illustrated): five founders and the host, labeled "illustration" (Gemini, `people: true`, 6; cutout yes).
- Local FLUX (`scripts/localart.py`): the pitch fair (1, 16:9), five booth products (5, 1:1).
- Drawn in code: sliders, the jar, the spread chart and future cards.
About 12 images.

## Voice
Two bank voices, each unique in this batch: `upbeat-guide` as the host; `knowing-guide` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.run + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `booth`: "Tap a booth."
- how `split`: "Move the sliders or tap Buy the basket."
- how `forward`: "Tap Fast-forward."
- how `many`: "Tap Run 100 futures."
- how `card`: "Tap a future card."
- event, whole, spread out.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: a seeded outcome model (half fold, three in ten about even, three in twenty triple, one in twenty ten times), the one-future playback, the 100-future spread chart.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Split | Put it all on one booth | The spread chart shows half of futures at zero. |
| Futures | Run one future | The comparison needs 100. |
| Cards | Skip the cards | The end asks what one idea added. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `booth`; `split`.
2. `forward`.
3. `many`; `card`.
4. Spread out (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NSPFE Investing and C3 D2.Eco.7.6-8 wording | data/standards/nspfe-2021.txt | data/standards/c3-indicators.txt and data/modules.csv | yes |
| Most young businesses fail or stay small; about a third survive ten years | U.S. Bureau of Labor Statistics, Business Employment Dynamics, "Establishment age and survival" | U.S. Small Business Administration Office of Advocacy (2024), "Frequently Asked Questions About Small Business" | yes |
| Diversification lowers the chance of losing everything without raising the average | U.S. Securities and Exchange Commission, Investor.gov, "Diversification" | FINRA, "Asset Allocation and Diversification" | yes |
| New businesses create a large share of new jobs | U.S. Census Bureau, Business Dynamics Statistics | Haltiwanger, Jarmin and Miranda (2013), "Who Creates Jobs? Small versus Large versus Young", Review of Economics and Statistics | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad s27, 2026-11-10): the model averages 1.25 times the money for one pick and for the basket; one pick ends at zero 50 percent of the time, the basket 3.1 percent (0.5 to the fifth); contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 fair and card; at 680x425 card as a sheet.
2. A split and the basket are each run 100 times and compared. (NSPFE Investing)
3. Future cards are read and one idea's effect on the town named. (D2.Eco.7.6-8)
4. No picks or advice; all companies are made up.
5. Outcome odds are labeled simulated and sourced.
6. `Read` reads every booth and card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: final results only; no network requests.

## Open questions
None.
